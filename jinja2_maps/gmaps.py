# -*- coding: UTF-8 -*-

from .base import _make_url_filter

# http://stackoverflow.com/a/25993441/735926
gmaps_url = _make_url_filter(
        "gmaps_url", "Google Maps",
        "https://www.google.com/maps/place/{lat},{lng}/@{lat},{lng},{zoom}z",
        zoom=16)
