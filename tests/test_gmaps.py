# -*- coding: UTF-8 -*-

from base import TestCase

from jinja2_maps.gmaps import gmaps_url

class TestGmaps(TestCase):

    def test_url_dict(self):
        url = "https://www.google.com/maps/place/12.34,56.78/@12.34,56.78,42z"
        self.assertEquals(url,
                gmaps_url(dict(latitude=12.34, longitude=56.78), zoom=42))

