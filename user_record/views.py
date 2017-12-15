# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views.generic import ListView

from music_store.utils import dictfetchall
# uid = '5367111875' 
# Create your views here.
def user_purchases(uid):
    with connection.cursor() as cursor:
        cursor.execute(
            "select s.name as song_name, a.name as artist, g.name as genre, s.`releaseDate` as rd, s.numDownloads "+
            "from purchases p, songs s, genres as g, artists as a "+
            "where "+
            "p.uid='" + uid + "' and s.sid=p.sid "+
            "and s.aid = a.aid "+
            "and s.gid = g.gid"
        )
        purchases = dictfetchall(cursor,fetchall=True)
    return purchases

def user_details(uid):
    with connection.cursor() as cursor:
        cursor.execute(
        "select * "+
        "from users u "+
        "where u.uid='" + uid + "'"
        )
        details = dictfetchall(cursor,fetchall=True)
    return details

def user_feedbacks(uid):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM feedbacks INNER JOIN songs WHERE feedbacks.sid = songs.sid AND uid='" + uid + "'" 
        )
        feedbacks = dictfetchall(cursor,fetchall=True)
    return feedbacks

def user_ratings(uid):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT r.uid AS uid, r.fuid as fuid, r.sid as sid, r.score as usefulness, f.score as score, f.comments as comments, f.postDate as postDate, u.login as username FROM ratings r INNER JOIN feedbacks f ON f.uid = r.fuid AND f.sid = r.sid INNER JOIN users u on f.uid = u.uid AND r.uid='" + uid + "'" 
        )
        ratings = dictfetchall(cursor,fetchall=True)
    return ratings


class User_Record_View(ListView):
    template_name = "user_record/user_record.html"

    def get_queryset(self):
        uid = self.kwargs['pk']
        purchases = user_purchases(uid)

        return purchases

    def get_context_data(self, **kwargs):
        context = super(User_Record_View, self).get_context_data(**kwargs)
        uid = self.kwargs['pk']
        context['details'] = user_details(uid)
        context['purchases'] = user_purchases(uid)
        context['feedbacks'] = user_feedbacks(uid)
        context['ratings'] = user_ratings(uid)
        return context

