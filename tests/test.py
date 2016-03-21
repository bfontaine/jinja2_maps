# -*- coding: UTF-8 -*-
import sys
from os.path import dirname
from base import unittest, TestCase

if __name__ == "__main__":
    here = dirname(__file__)
    sys.path.insert(0, here+"/..")

from jinja2 import Environment
import jinja2_maps

class TestJinja2Maps(TestCase):
    def test_version(self):
        self.assertRegexpMatches(jinja2_maps.__version__, r"^\d+\.\d+\.\d+")

    def test_activate_filters(self):
        env = Environment()
        jinja2_maps.activate_filters(env)
        self.assertIn("gmaps_url", env.filters)

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(here)
    t = unittest.TextTestRunner().run(suite)
    if not t.wasSuccessful():
        sys.exit(1)
