# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import connection

from utils import dictfetchall

# Create your views here.
def music_info(request, pk):
	''' gets the primary key of the queried music and displays the info '''
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Songs WHERE sid = %s", [pk])
		music = dictfetchall(cursor)
		
		cursor.execute("SELECT uid, sid, score, postDate, comments, login FROM Feedbacks NATURAL JOIN Users WHERE sid=%s", [pk])
		feedbacks = dictfetchall(cursor, fetchall = True)

		for feedback in feedbacks: # iterate through feedbacks for a particular song to get ratings
			fuid = feedback['uid'] # the person who made the feedback
			cursor.execute("SELECT AVG(score) FROM Ratings GROUP BY fuid,sid HAVING fuid = %s AND sid = %s", [fuid, pk])
			feedback['rating'] = '{:.1f}'.format(cursor.fetchone()[0])
		
	return render(request, 'feedback_rating/music_info.html', {'music':music, 'feedbacks':feedbacks})