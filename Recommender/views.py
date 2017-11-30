# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def recommend(request):

    # return HttpResponse("Recommender motherfuckkkaazzz")
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

       "SELECT s.sid, s.name, s.aid, s.gid, s.releaseDate, s.numDownloads, s.numLicense " 
       "FROM songs as s, (SELECT DISTINCT sid  FROM Purchases, (SELECT uid FROM Purchases " 
													            "WHERE Purchases.sid = '0000000001' AND Purchases.uid <> '1543016742') AS similar_users " 
			             "WHERE Purchases.uid = similar_users.uid AND Purchases.sid <> '0000000001') AS recommendations "
       "WHERE s.sid = recommendations.sid " 
       "ORDER by s.numDownloads DESC"
        )
        row = dictfetchall(cursor)



    return render(request, 'Recommender/recommender.html', {'recommendations':row})

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]