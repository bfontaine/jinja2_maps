# -*- coding: UTF-8 -*-

from .osm import osm_map, osm_url
from .gmaps import gmaps_url
from .apple_maps import apple_maps_url
from .bing_maps import bing_maps_url
from .mappy import mappy_url

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
    )


def activate_filters(env):
    """
    Activate all filters on a given environment. If using Flask calling
    `activate_filters(app.jinja_env)` at the top of your `app.py` should be
    sufficient.
    """
    env.filters.update(filters())
