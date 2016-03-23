# -*- coding: UTF-8 -*-

from base import TestCase

import jinja2_maps
from jinja2_maps.bing_maps import bing_maps_url

class TestBingMaps(TestCase):

    def test_url_filter_exists(self):
        self.assertIn("bing_maps_url", jinja2_maps.filters())

    def test_url_dict(self):
        url = "https://www.bing.com/mapspreview?&cp=12.34~56.78&lvl=2"
        self.assertEquals(url,
                bing_maps_url(dict(latitude=12.34, longitude=56.78), zoom=2))

    def test_url_dict_no_zoom(self):
        url = "https://www.bing.com/mapspreview?&cp=12.34~56.78&lvl=16"
        self.assertEquals(url,
                bing_maps_url(dict(latitude=12.34, longitude=56.78)))

