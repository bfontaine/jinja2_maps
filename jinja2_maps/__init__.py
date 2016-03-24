# -*- coding: UTF-8 -*-

from .osm import osm_map, osm_url
from .urls import gmaps_url, apple_maps_url, bing_maps_url, mappy_url, here_url
from .urls import arcgis_url, wikimapia_url, yandex_maps_url

# Ensure imported functions are not exported
__all__ = ["__version__", "filters", "activate_filters"]

__version__ = "0.2.0"


def filters():
    return dict(
        gmaps_url=gmaps_url,
        osm_map=osm_map,
        osm_url=osm_url,
        apple_maps_url=apple_maps_url,
        bing_maps_url=bing_maps_url,
        mappy_url=mappy_url,
        arcgis_url=arcgis_url,
        here_url=here_url,
        wikimapia_url=wikimapia_url,
        yandex_maps_url=yandex_maps_url,

        # Aliases
        google_maps_url=gmaps_url,
    )


def activate_filters(env):
    """
    Activate all filters on a given environment. If using Flask calling
    `activate_filters(app.jinja_env)` at the top of your `app.py` should be
    sufficient.
    """
    env.filters.update(filters())
