# -*- coding: UTF-8 -*-

from base import TestCase

import jinja2_maps
from jinja2_maps.urls import gmaps_url

class TestGmaps(TestCase):

    def test_url_filter_exists(self):
        self.assertIn("gmaps_url", jinja2_maps.filters())

    def test_url_dict(self):
        url = "https://www.google.com/maps/place/12.34,56.78/@12.34,56.78,42z"
        self.assertEquals(url,
                gmaps_url(dict(latitude=12.34, longitude=56.78), zoom=42))

    def test_url_dict_no_zoom(self):
        url = "https://www.google.com/maps/place/12.34,56.78/@12.34,56.78,16z"
        self.assertEquals(url,
                gmaps_url(dict(latitude=12.34, longitude=56.78)))

