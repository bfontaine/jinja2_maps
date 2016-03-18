===========
jinja2_maps
===========

``jinja2_maps`` is a set of filters to display locations in Jinja2 templates.

Install
-------

.. code-block::

    pip install jinja2_maps

Support
-------

====           ===  ===
               URL  Map
OpenStreetMap  Yes  Yes
Google Maps    Yes  -
Bing Maps      -    -
Apple Maps     -    -
====           ===  ===

Usage
-----

All filters take a location as a dict with ``latitude`` and ``longitude`` keys.
You can also pass an object with these attributes.

Before using any template you need to add the filters to your Jinja2
environment: ::

  from jinja2_maps import activate_filters
  activate_filters(your_env)

If using Flask you can do the following: ::

  from jinja2_maps import activate_filters
  activate_filters(app.jinja_env)

URLs
~~~~

::
  <a href="{{ your_location | osm_url }}">Check on OpenStreetMap</a>
  <a href="{{ your_location | gmaps_url }}">Check on Google Maps</a>

Maps
~~~~

::
  {{ your_location | osm_map(width=500, height=400) }}
