# -*- coding: UTF-8 -*-

from base import TestCase

from jinja2_maps.base import _normalize_location

class Location(object):
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

class TestBase(TestCase):

    def test_normalize_location_dict(self):
        d = {"latitude": 42.0, "longitude": 17.0}
        self.assertEquals(d, _normalize_location(d))

    def test_normalize_location_nondict(self):
        self.assertEquals({"latitude": 42.3, "longitude": 17.1},
                _normalize_location(Location(latitude=42.3, longitude=17.1)))
        self.assertEquals({"latitude": 41.3, "longitude": 16.1},
                _normalize_location(Location(lat=41.3, lng=16.1)))
