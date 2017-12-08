# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views.generic import ListView

from music_store.utils import dictfetchall

# Create your views here.
def recommend():

    sid = '0000000001'
    uid = '5367111875'

    with connection.cursor() as cursor:
        # cursor.execute(
        # "CREATE view recommendations as"+
        # "SELECT DISTINCT sid  FROM Purchases, (SELECT uid FROM Purchases "+
        #                         "WHERE Purchases.sid = '0000000001' AND Purchases.uid <> '1543016742') AS similar_users "+
        # "WHERE Purchases.uid = similar_users.uid AND Purchases.sid <> '0000000001'"
        # )
        # cursor.execute(
        # "SELECT s.sid, s.name, s.aid, s.gid, s.releaseDate, s.numDownloads, s.numLicense "+
        # "FROM songs as s "+
        # "RIGHT JOIN recommendations ON s.sid = recommendations.sid "+
        # "ORDER by s.numDownloads DESC"
        # )

        cursor.execute(
       "SELECT g.name as genre, a.name artist, s.sid, s.name, s.aid, s.gid, s.releaseDate, s.numDownloads, s.numLicense " 
       "FROM artists as a, genres as g, songs as s, (SELECT DISTINCT sid  FROM Purchases, (SELECT uid FROM Purchases " 
													 "WHERE Purchases.sid = %s AND Purchases.uid <> %s) AS similar_users " 
			             "WHERE Purchases.uid = similar_users.uid AND Purchases.sid <> %s) AS recommendations "
       "WHERE s.sid = recommendations.sid AND s.aid=a.aid AND s.gid=g.gid " 
       "ORDER by s.numDownloads DESC",[sid,uid,sid]
        )
        songs = dictfetchall(cursor,fetchall=True)


    return songs
    # return render(request, 'recommender.html', songs)


class RecommenderView(ListView):
    template_name = "recommender.html"


    def get_queryset(self):
        songs = recommend()
        return songs



#trigger
#don't use sorting using python
#HTML links to say built in queries you can do