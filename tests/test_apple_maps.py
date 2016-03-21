# -*- coding: UTF-8 -*-

from base import TestCase

import jinja2_maps
from jinja2_maps.apple_maps import apple_maps_url

class TestAppleMaps(TestCase):

    def test_url_filter_exists(self):
        self.assertIn("apple_maps_url", jinja2_maps.filters())

    def test_url_dict(self):
        url = "https://maps.apple.com/?ll=12.34,56.78&z=2&t=&q="
        self.assertEquals(url,
                apple_maps_url(dict(latitude=12.34, longitude=56.78), zoom=2))

    def test_url_dict_no_zoom(self):
        url = "https://maps.apple.com/?ll=12.34,56.78&z=16&t=&q="
        self.assertEquals(url,
                apple_maps_url(dict(latitude=12.34, longitude=56.78)))

