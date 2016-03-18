# -*- coding: UTF-8 -*-

from .base import urlencode, map_filter, url_filter
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

    iframe = '<iframe %s src="http://www.openstreetmap.org/export/embed.html?%s"></iframe>' % (
        html_attrs,
        urlencode(params),
    )

    if eval_ctx.autoescape:
        return Markup(iframe)
    return iframe

@url_filter
def osm_url(loc, zoom=16):
    """
    Given a dict-like with ``latitude`` and ``longitude`` attributes write an
    OpenStreetMap URL for this location.
    """
    lat = loc["latitude"]
    lng = loc["longitude"]

    return "http://www.openstreetmap.org/?mlat=%f&amp;mlon=%f#map=%d/%f/%f" % (
        lat, lng, zoom, lat, lng)
