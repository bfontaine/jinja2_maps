# -*- coding: UTF-8 -*-

from .base import _make_url_filter

# https://developer.apple.com/library/ios/featuredarticles/iPhoneURLScheme_Reference/MapLinks/MapLinks.html
apple_maps_url = _make_url_filter(
        "apple_maps_url", "Apple Maps",
        "https://maps.apple.com/?ll={lat:g},{lng:g}&z={zoom}&t={t}&q={q}",
        zoom=16, t="", q="")
