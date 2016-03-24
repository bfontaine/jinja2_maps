# -*- coding: UTF-8 -*-

from .base import _make_url_filter

# https://developer.apple.com/library/ios/featuredarticles/iPhoneURLScheme_Reference/MapLinks/MapLinks.html
apple_maps_url = _make_url_filter(
        "apple_maps_url", "Apple Maps",
        "https://maps.apple.com/?ll={lat:g},{lng:g}&z={zoom}&t={t}&q={q}",
        zoom=16, t="", q="")

bing_maps_url = _make_url_filter(
        "bing_maps_url", "Bing Maps",
        "https://www.bing.com/mapspreview?&cp={lat}~{lng}&lvl={zoom}",
        zoom=16)

# http://stackoverflow.com/a/25993441/735926
gmaps_url = _make_url_filter(
        "gmaps_url", "Google Maps",
        "https://www.google.com/maps/place/{lat},{lng}/@{lat},{lng},{zoom}z",
        zoom=16)

mappy_url = _make_url_filter(
        "mappy_url", "Mappy",
        "http://{locale}.mappy.com/#/M2/THome/N0,0,{lat},{lng}/Z{zoom}/",
        zoom=16, locale="en")
