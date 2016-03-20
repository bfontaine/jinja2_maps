# -*- coding: UTF-8 -*-

from base import TestCase

from jinja2_maps.osm import osm_url

class TestOsm(TestCase):

    def test_url_dict(self):
        url = "https://www.openstreetmap.org/?mlat=12.34&mlon=56.78" \
                "#map=42/12.3400/56.7800"
        self.assertEquals(url,
                osm_url(dict(latitude=12.34, longitude=56.78), zoom=42))
