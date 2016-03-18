# -*- coding: UTF-8 -*-

from .osm import osm_map, osm_url
from .gmaps import gmaps_url

__version__ = "0.1.0"

def filters():
    return dict(
        gmaps_url=gmaps_url,
        osm_map=osm_map,
        osm_url=osm_url,
    )

def activate_filters(env):
    """
    Activate all filters on a given environment. If using Flask calling
    `activate_filters(app.jinja_env)` at the top of your `app.py` should be
    sufficient.
    """
    env.filters.update(filters())
