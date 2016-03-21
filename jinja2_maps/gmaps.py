# -*- coding: UTF-8 -*-

from .base import _make_url_filter

URL_FMT = "https://www.google.com/maps/place/{lat},{lng}/@{lat},{lng},{zoom}z"

gmaps_url = _make_url_filter("gmaps_url", "Google Maps", URL_FMT)
