# -*- coding: UTF-8 -*-

from .base import url_filter

URL_FMT = "https://www.google.com/maps/place/{lat},{lon}/@{lat},{lon},{zoom}z"


@url_filter
def gmaps_url(loc, zoom=16):
    """
    Given a dict-like with ``latitude`` and ``longitude`` attributes write a
    Google Maps URL for this location.
    """
    return URL_FMT.format(lat=loc["latitude"], lon=loc["longitude"], zoom=zoom)
