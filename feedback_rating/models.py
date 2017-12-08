# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django import forms

# Create your models here.
class FeedbackForm(forms.Form):
	'''Customized form that does not utilize Django's ORM to retrieve POST data'''
	score_choices = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]

	score = forms.ChoiceField(choices=score_choices)
	comments = forms.CharField(max_length=250)

class SortForm(forms.Form):
	count = forms.IntegerField()
	filter_choices = [('rating', 'Ratings'), ('postDate', 'Post Date')]
	sort = forms.ChoiceField(choices=filter_choices)

class selectMusicForm(forms.Form):
    sid = forms.CharField(required=True,max_length=10,min_length=10)
