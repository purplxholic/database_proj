# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views.generic import ListView

from music_store.utils import dictfetchall

# Create your views here.
def recommend(uid,sid):

    sid = sid
    uid = uid

    with connection.cursor() as cursor:

        cursor.execute(
       "SELECT g.name as genre, a.name artist, s.sid, s.name, s.aid, s.gid, s.releaseDate, s.numDownloads, s.numLicense "
       "FROM Artists as a, Genres as g, Songs as s, (SELECT DISTINCT sid  FROM Purchases, (SELECT uid FROM Purchases "
													 "WHERE Purchases.sid = %s AND Purchases.uid <> %s) AS similar_users "
			             "WHERE Purchases.uid = similar_users.uid AND Purchases.sid <> %s) AS recommendations "
       "WHERE s.sid = recommendations.sid AND s.aid=a.aid AND s.gid=g.gid "
       "ORDER by s.numDownloads DESC",[sid,uid,sid]
        )
        songs = dictfetchall(cursor,fetchall=True)


    return songs
    # return render(request, 'recommender.html', songs)


class RecommenderView(ListView):
    template_name = "recommender_/recommender.html"


    def get_queryset(self):
        uid = self.kwargs['pk']
        sid = self.kwargs['sk']
        songs = recommend(uid,sid)
        return songs
