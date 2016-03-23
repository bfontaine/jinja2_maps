# -*- coding: UTF-8 -*-

from .base import _make_url_filter

bing_maps_url = _make_url_filter(
        "bing_maps_url", "Bing Maps",
        "https://www.bing.com/mapspreview?&cp={lat}~{lng}&lvl={zoom}",
        zoom=16)
