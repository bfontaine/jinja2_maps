# -*- coding: UTF-8 -*-

from base import TestCase

import jinja2_maps
from jinja2_maps.urls import mappy_url

class TestMappy(TestCase):

    def test_url_filter_exists(self):
        self.assertIn("mappy_url", jinja2_maps.filters())

    def test_url_dict(self):
        url = "http://en.mappy.com/#/M2/THome/N0,0,12.34,56.78/Z2/"
        self.assertEquals(url,
                mappy_url(dict(latitude=12.34, longitude=56.78), zoom=2))

    def test_url_dict_no_zoom(self):
        url = "http://en.mappy.com/#/M2/THome/N0,0,12.34,56.78/Z16/"
        self.assertEquals(url,
                mappy_url(dict(latitude=12.34, longitude=56.78)))

    def test_url_dict_locale(self):
        url = "http://fr.mappy.com/#/M2/THome/N0,0,12.34,56.78/Z16/"
        self.assertEquals(url,
                mappy_url(dict(latitude=12.34, longitude=56.78), locale="fr"))


