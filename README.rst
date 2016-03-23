===========
jinja2_maps
===========

``jinja2_maps`` is a set of filters to display locations in Jinja2 templates.

.. image:: https://travis-ci.org/bfontaine/jinja2_maps.svg?branch=master
    :target: https://travis-ci.org/bfontaine/jinja2_maps

Install
-------

.. code-block::

    pip install jinja2_maps

Support
-------

=============  ===  ===
Service        URL  Map
=============  ===  ===
OpenStreetMap  Yes  Yes
Google Maps    Yes  -
Apple Maps     Yes  -
Bing Maps      Yes  -
Mappy          Yes  -
=============  ===  ===

Both Python 2.x and 3.x are supported.

Usage
-----

All filters take a location as a dict with ``latitude`` and ``longitude`` keys.
You can also pass an object with these attributes.

Before using any template you need to add the filters to your Jinja2
environment:

.. code-block:: python

  from jinja2_maps import activate_filters
  activate_filters(your_env)

If using Flask you can do the following:

.. code-block:: python

  from jinja2_maps import activate_filters
  activate_filters(app.jinja_env)

URLs
~~~~

.. code-block:: html+jinja

  <a href="{{ your_location | osm_url }}">Check on OpenStreetMap</a>
  <a href="{{ your_location | gmaps_url }}">Check on Google Maps</a>
  <a href="{{ your_location | apple_maps_url }}">Check in Maps</a>
  <a href="{{ your_location | bing_maps_url }}">Check on Bing Maps</a>
  <a href="{{ your_location | mappy_url }}">Check on Mappy</a>

URLs also support giving the zoom level (default is ``16``):

.. code-block:: html+jinja

  <a href="{{ your_location | osm_url(zoom=12) }}">Check on OpenStreetMap</a>

Maps
~~~~

.. code-block:: html+jinja

  {{ your_location | osm_map(width=500, height=400) }}
