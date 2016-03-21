# -*- coding: UTF-8 -*-

try:
    from urllib import urlencode
except ImportError:  # Python 3
    from urllib.parse import urlencode

from jinja2 import evalcontextfilter


def _normalize_location(loc):
    """
    Return a dictionary that represents the given location. If it's already a
    dictionary it's returned as-is but if not we try different attributes to
    get the latitude (``latitude`` or ``lat``) and longitude (``longitude``,
    ``lng``, or ``lon``).
    """
    if isinstance(loc, dict):
        return loc

    d = {}
    # Try different attributes for each one
    guesses = {
        "latitude": ("latitude", "lat"),
        "longitude": ("longitude", "lng", "lon"),
    }
    for attr, ks in guesses.items():
        for k in ks:
            if hasattr(loc, k):
                d[attr] = float(getattr(loc, k))
                break

    return d


def _make_url_filter(name, service, fmt, **args):
    def _filter(loc, **kw):
        loc = _normalize_location(loc)

        params = dict(args)
        params.update(kw)

        return fmt.format(lat=loc["latitude"], lng=loc["longitude"], **params)

    _filter.__name__ = name
    _filter.__doc__ = """
        Write a URL for {service} from a dict with latitude/longitude keys.
    """.format(service=service)

    return _filter


def map_filter(fn):
    """
    Wrap a function as a filter that returns HTML to display a map.
    """

    @evalcontextfilter
    def _filter(eval_ctx, loc, *args, **kw):
        return fn(eval_ctx, _normalize_location(loc), *args, **kw)

    _filter.__name__ = fn.__name__
    _filter.__doc__ = fn.__doc__
    return _filter

# silent Pyflakes
urlencode
