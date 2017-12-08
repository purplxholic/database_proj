# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from .forms import statisticsForm
def index(request):
    form_class = statisticsForm

    if request.method=='POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            topno = request.POST.get('howhigh')
            type_ofstats = request.POST.get('stats')
            return HttpResponseRedirect('./stats_choice/'+type_ofstats+"/"+topno)
    return render(request,'statistics/index.html',{'form':form_class})


'''
stats_choice reads the choice of statistics that user wants to be returned
depending on choice, load the different methods to query
returned value of the functions below would be in INT
'''
def stats_choice(request,choice,top_no):
    results = []

    correct_req = True
    exceeded = False
    query_length = 0
    if choice == "all":
        exceeded_s = False
        exceeded_a = False
        exceeded_g = False
        results_s=[]
        results_a=[]
        results_g=[]
        results_s, exceeded_s, query_length_s = song_stats(top_no)
        results_a, exceeded_a, query_length_a = artist_stats(top_no)
        results_g, exceeded_g, query_length_g = genre_stats(top_no)
        context = {"results_s" : results_s,"results_a" : results_a,"results_g" : results_g,"correct_req":correct_req,"type":choice,"no":top_no,"exceeded_s":exceeded_s,"exceeded_a":exceeded_a,"exceeded_g":exceeded_g,"query_length_s":query_length_s,"query_length_a":query_length_a,"query_length_g":query_length_g}

    else:

        if choice == "song":

            results, exceeded, query_length = song_stats(top_no)
        elif choice == "artist":

            results, exceeded, query_length = artist_stats(top_no)
        elif choice == "genre":

            results, exceeded, query_length = genre_stats(top_no)
        else:
            correct_req = False
            results = "Invalid Choice. Your choice was " + choice + ". Available options: song,artist,genre and all. "
        choice   = choice.title()
        context = {"results" : results,"correct_req":correct_req,"type":choice,"no":top_no,"exceeded":exceeded,"query_length":query_length}
    return render(request,'statistics/top.html',context)
#displays user stated number of top songs
def song_stats(top_no):
    song_names = []
    query_length = int(top_no)
    exceeded = False
    with connection.cursor() as cursor:
        # cursor.execute("SELECT COUNT(*) FROM Purchases GROUP BY sid ORDER BY DESC")
        cursor.execute("SELECT S.name FROM Purchases P, Songs S WHERE P.sid = S.sid GROUP BY P.sid ORDER BY COUNT(*) DESC")
        results = cursor.fetchall() # get all the results

        #to handle if requested no. of top exceeds queried number
        if (len(results) < query_length):
            query_length = len(results)
            exceeded = True

        #results returned should be in ((xxx),(yyy))
        for i in range(query_length):
            name = results[i][0]
            song_names.append(name )

    return song_names,exceeded, str(query_length)

#displays user stated number of top artists
def artist_stats(top_no):
    artist_names = []
    query_length = int(top_no)
    exceeded = False
    with connection.cursor() as cursor:
        cursor.execute("SELECT A.name FROM Purchases P, Songs S, Artists A WHERE P.sid = S.sid AND S.aid = A.aid GROUP BY A.aid ORDER BY COUNT(*) DESC")
        results = cursor.fetchall() # get all the results

        #to handle if requested no. of top exceeds queried number
        if (len(results) < query_length):
            query_length = len(results)
            exceeded = True

        for i in range(query_length):
            name = results[i][0]
            artist_names.append(name)

    return artist_names,exceeded, str(query_length)

#displays user stated number of top genre
def genre_stats(top_no):
    genre_names = []
    query_length = int(top_no)
    exceeded = False
    with connection.cursor() as cursor:
        cursor.execute("SELECT G.name FROM Purchases P, Songs S, Genres G WHERE P.sid = S.sid AND G.gid = S.gid GROUP BY G.gid ORDER BY COUNT(*) DESC")
        results = cursor.fetchall() # get all the results

        #to handle if requested no. of top exceeds queried number
        if (len(results) < query_length):
            query_length = len(results)
            exceeded = True

        for i in range(query_length):
            name = results[i][0]
            genre_names.append(name)

    return genre_names,exceeded, str(query_length)
