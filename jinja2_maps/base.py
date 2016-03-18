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
    get the latitude and longitude.
    """
    if isinstance(loc, dict):
        return loc

    d = {}
    # Try different attributes for each one
    guesses = {
        "latitude": ("latitude", "lat"),
        "longitude": ("longitude", "lng", "long", "lon"),
    }
    for attr, ks in guesses.items():
        for k in ks:
            if hasattr(loc, k):
                d[attr] = getattr(loc, k)
                break

    return d

def _copy_function_attrs(origin, target):
    target.__name__ = origin.__name__
    target.__doc__ = origin.__doc__

def url_filter(fn):
    """
    Wrap a function as a filter that returns an URL.
    """
    def _filter(loc, *args, **kw):
        return fn(_normalize_location(loc), *args, **kw)

    _copy_function_attrs(fn, _filter)
    return _filter

def map_filter(fn):
    """
    Wrap a function as a filter that returns HTML to display a map.
    """

    @evalcontextfilter
    def _filter(eval_ctx, loc, *args, **kw):
        return fn(eval_ctx, _normalize_location(loc), *args, **kw)

    _copy_function_attrs(fn, _filter)
    return _filter

# silent Pyflakes
if False:
    urlencode
