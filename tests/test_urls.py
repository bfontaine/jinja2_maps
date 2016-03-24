# -*- coding: UTF-8 -*-

from base import TestCase

import jinja2_maps
from jinja2_maps.urls import apple_maps_url, bing_maps_url, gmaps_url
from jinja2_maps.urls import mappy_url

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


class TestGmaps(TestCase):

    def test_url_filter_exists(self):
        self.assertIn("gmaps_url", jinja2_maps.filters())
        self.assertIn("google_maps_url", jinja2_maps.filters())

    def test_url_dict(self):
        url = "https://www.google.com/maps/place/12.34,56.78/@12.34,56.78,42z"
        self.assertEquals(url,
                gmaps_url(dict(latitude=12.34, longitude=56.78), zoom=42))

    def test_url_dict_no_zoom(self):
        url = "https://www.google.com/maps/place/12.34,56.78/@12.34,56.78,16z"
        self.assertEquals(url,
                gmaps_url(dict(latitude=12.34, longitude=56.78)))


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


