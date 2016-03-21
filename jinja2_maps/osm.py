# -*- coding: UTF-8 -*-

from .base import urlencode, map_filter, _make_url_filter
from jinja2 import Markup, escape

_osm_default_attrs = dict(
    width=500,
    height=400,
    frameborder=0,
    scrolling="no",
    marginheight=0,
    marginwidth=0,
)

# roughly equivalent to zoom level 17
# (note: this also depends on the width/height proportions)
LAT_PADDING = 0.00333
LNG_PADDING = 0.0063589

ROOT = "https://www.openstreetmap.org"

URL_FMT = "{root}/?mlat={lat:g}&mlon={lng:g}#map={zoom}/{lat:.4f}/{lng:.4f}"
MAP_FMT = '<iframe {attrs} src="{root}/export/embed.html?{params}"></iframe>'

osm_url = _make_url_filter(
        "osm_url", "OpenStreetMap", URL_FMT, root=ROOT, zoom=16)


@map_filter
def osm_map(eval_ctx, loc, **kw):
    lat = loc["latitude"]
    lng = loc["longitude"]
    layer = kw.pop("layer", "mapnik")

    attrs = dict(_osm_default_attrs)
    attrs.update(kw)

    bbox = [lng-LNG_PADDING, lat-LAT_PADDING, lng+LNG_PADDING, lat+LAT_PADDING]

    params = {
            "bbox": ",".join([str(p) for p in bbox]),
            "layer": layer,
            "marker": "%f,%f" % (lat, lng),
    }

    html_attrs = " ".join(
            ['%s="%s"' % (escape(k), escape(v)) for k, v in attrs.items()])

    iframe = MAP_FMT.format(
            attrs=html_attrs, params=urlencode(params), root=ROOT)

    if eval_ctx.autoescape:
        return Markup(iframe)
    return iframe
