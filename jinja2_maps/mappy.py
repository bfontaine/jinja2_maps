# -*- coding: UTF-8 -*-

from .base import _make_url_filter

mappy_url = _make_url_filter(
        "mappy_url", "Mappy",
        "http://{locale}.mappy.com/#/M2/THome/N0,0,{lat},{lng}/Z{zoom}/",
        zoom=16, locale="en")
