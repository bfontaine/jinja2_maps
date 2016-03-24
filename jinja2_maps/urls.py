# -*- coding: UTF-8 -*-

from .base import _make_url_filter

# Note ArcGIS uses <longitude>,<latitude> while all others use
# <latitude>,<longitude>
# https://doc.arcgis.com/en/arcgis-online/reference/use-url-parameters.htm
arcgis_url = _make_url_filter(
        "arcgis_url", "ArcGIS",
        ("https://www.arcgis.com/home/webmap/viewer.html"
            "?center={lng},{lat}&level={zoom}"),
        zoom=16)

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

here_url = _make_url_filter(
        "here_url", "HERE Maps",
        "https://maps.here.com/?map={lat},{lng},{zoom},{layer}",
        zoom=16, layer="normal")

mappy_url = _make_url_filter(
        "mappy_url", "Mappy",
        "http://{locale}.mappy.com/#/M2/THome/N0,0,{lat},{lng}/Z{zoom}/",
        zoom=16, locale="en")

wikimapia_url = _make_url_filter(
        "wikimapia_url", "Wikimapia",
        ("http://wikimapia.org/"
            "#lang={locale}&lat={lat}&lon={lng}&z={zoom}&m={m}"),
        zoom=16, m="w", locale="en")

yandex_maps_url = _make_url_filter(
        "yandex_maps_url", "Yandex Maps",
        "https://yandex.com/maps/105075/{place}/?ll={lat},{lng}&z={zoom}",
        # {place} can be anything; it doesn't affect the display; the
        # coordinates do.
        zoom=16, place="place")
