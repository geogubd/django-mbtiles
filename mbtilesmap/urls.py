# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from . import MBTILES_NAME_PATTERN
from views import tile, grid, jsonp


urlpatterns = patterns('',
    url(r'^(?P<name>%s)/(?P<z>(\d+|\{z\}))/(?P<x>(\d+|\{x\}))/(?P<y>(\d+|\{y\})).png$' % MBTILES_NAME_PATTERN, tile, name="tile"),
    url(r'^(?P<name>%s)/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).grid.json$' % MBTILES_NAME_PATTERN, grid, name="grid"),
    url(r'^(?P<name>%s).jsonp$' % MBTILES_NAME_PATTERN, jsonp, name="jsonp"),
)
