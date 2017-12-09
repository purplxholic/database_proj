# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views.generic import ListView

from music_store.utils import dictfetchall
uid = '5367111875'
# Create your views here.
def user_purchases():
    with connection.cursor() as cursor:
        cursor.execute(
            "select s.name as song_name, a.name as artist, g.name as genre, s.`releaseDate` as rd "+
            "from purchases p, songs s, genres as g, artists as a "+
            "where "+
            "p.uid='5367111875' and s.sid=p.sid "+
            "and s.aid = a.aid "+
            "and s.gid = g.gid"
        )
        purchases = dictfetchall(cursor,fetchall=True)
    return purchases

def user_details():
    with connection.cursor() as cursor:
        cursor.execute(
        "select * "+
        "from users u "+
        "where u.uid='5367111875'"
        )
        purchases = dictfetchall(cursor,fetchall=True)
    return purchases


class User_Record_View(ListView):
    template_name = "user_record/user_record.html"


    def get_queryset(self):
        purchases = user_purchases()
        ud = user_details()


        return purchases

