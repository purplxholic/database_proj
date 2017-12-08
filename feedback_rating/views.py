# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import connection

from music_store.utils import dictfetchall
from feedback_rating.models import FeedbackForm, SortForm,selectMusicForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

# Create your views here.
def index(request):
	selectMusic_form = selectMusicForm()

	#redirect when you enter the song sid
	if request.method == "POST":
		selectMusic_form = selectMusicForm(request.POST)
		if selectMusic_form.is_valid():
			cd = selectMusic_form.cleaned_data
			sid= cd.get('sid')
			return HttpResponseRedirect('/music/'+sid)
		
	return render(request,'feedback_rating/index.html',{'form':selectMusic_form})

def music_info(request, pk):
	''' gets the primary key of the queried music and displays the info '''
	feedback_form = FeedbackForm()
	sort_form = SortForm()

	numFeedbacks = 0

	# hardcoded for now as the user login system has not been implemented
	# for testing:
	# DELETE FROM Feedbacks WHERE uid='0928753099';
	# DELETE FROM Ratings WHERE uid='0928753099';
	uid = '0928753099'
	sorting = ''

	with connection.cursor() as cursor:
		if request.method == 'POST':
			if 'useless-btn' in request.POST:
				cursor.execute("INSERT INTO Ratings (uid, fuid, sid, score) VALUES (%s, %s, %s, %s)", [uid, request.POST['useless-btn'], pk, '0'])
			elif 'useful-btn' in request.POST:
				cursor.execute("INSERT INTO Ratings (uid, fuid, sid, score) VALUES (%s, %s, %s, %s)", [uid, request.POST['useful-btn'], pk, '1'])
			elif 'very-useful-btn' in request.POST:
				cursor.execute("INSERT INTO Ratings (uid, fuid, sid, score) VALUES (%s, %s, %s, %s)", [uid, request.POST['very-useful-btn'], pk, '2'])
			elif 'sort-feedback-btn' in request.POST:
				sort_form = SortForm(request.POST)
				if sort_form.is_valid():
					cd = sort_form.cleaned_data
					numFeedbacks = cd.get('count')
					sorting = cd.get('sort')
			else:
				feedback_form = FeedbackForm(request.POST)
				if feedback_form.is_valid():
					cd = feedback_form.cleaned_data
					cursor.execute("INSERT INTO Feedbacks (uid, sid, score, postDate, comments) VALUES (%s, %s, %s, %s, %s)", [uid, pk, cd.get('score'), datetime.date.today().strftime("%Y-%m-%d"), cd.get('comments')])

		cursor.execute("SELECT * FROM Songs WHERE sid = %s", [pk])
		music = dictfetchall(cursor)

		cursor.execute("SELECT uid, sid, score, postDate, comments, login FROM Feedbacks NATURAL JOIN Users WHERE sid=%s", [pk])
		feedbacks = dictfetchall(cursor, fetchall = True)

		for feedback in feedbacks: # iterate through feedbacks for a particular song to get ratings
			fuid = feedback['uid'] # the person who made the feedback
			cursor.execute("SELECT AVG(score) FROM Ratings GROUP BY fuid,sid HAVING fuid = %s AND sid = %s", [fuid, pk])
			r = cursor.fetchone()
			if r:
				feedback['rating'] = '{:.1f}'.format(r[0])
			else:
				feedback['rating'] = 0.0

		if numFeedbacks>0:
			feedbacks = sorted(feedbacks, key=lambda k:k[sorting], reverse=True)[:numFeedbacks]
			# feedbacks = feedbacks[:numFeedbacks]

	return render(request, 'feedback_rating/music_info.html', {'music':music, 'feedbacks':feedbacks, 'feedback_form':feedback_form, 'sort_form':sort_form})
