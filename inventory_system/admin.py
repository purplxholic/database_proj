# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Purchase)
admin.site.register(Feedback)
admin.site.register(Rating)