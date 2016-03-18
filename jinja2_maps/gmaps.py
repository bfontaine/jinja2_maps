# -*- coding: UTF-8 -*-

from .base import url_filter

@url_filter
def gmaps_url(loc, zoom=16):
    """
    Given a dict-like with ``latitude`` and ``longitude`` attributes write a
    Google Maps URL for this location.
    """
    lat = loc["latitude"]
    lon = loc["longitude"]

    return "https://www.google.com/maps/place/%f,%f/@%f,%f,%dz" % (
        lat, lon, lat, lon, zoom)
