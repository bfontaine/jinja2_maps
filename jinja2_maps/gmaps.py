# -*- coding: UTF-8 -*-

from .base import map_filter

@map_filter
def gmaps_url(eval_ctx, loc, zoom=16):
    """
    Given a dict-like with ``latitude`` and ``longitude`` attributes write a
    Google Maps URL for this location.
    """
    lat = loc["latitude"]
    lon = loc["longitude"]

    url = "https://www.google.com/maps/place/%f,%f/@%f,%f,%dz" % (
        lat, lon, lat, lon, zoom)

    return url
