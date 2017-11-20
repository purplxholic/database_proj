# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def index(request):
    return HttpResponse("Statistics function is working!")

'''
stats_choice reads the choice of statistics that user wants to be returned
depending on choice, load the different methods to query
returned value of the functions below would be in INT
'''
def stats_choice(request,choice,top_no):
    if choice == "song":
        return HttpResponse(song_stats(top_no))
    elif choice == "artist":
        return HttpResponse(artist_stats(top_no))
    elif choice == "genre":
        return HttpResponse(genre_stats(top_no))
    elif choice == "all":
        return song_stats(top_no),artist_stats(top_no),genre_stats(top_no),labels_stats(top_no)
    else:
        return HttpResponse("Invalid Choice. Options: song,artist,genre,label and all. Your choice:" + choice)
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
            song_names.append(name + " ")

    if exceeded :
        song_names.append("\nSorry! We could only return the top " + str(query_length))
    return song_names

#displays user stated number of top artists
#TODO: count no. of time artist appeared in the Purchases
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
            artist_names.append(name + " ")
    if exceeded :
        artist_names.append("\nSorry! We could only return the top " + str(query_length))
    return artist_names

#displays user stated number of top genre
def genre_stats(top_no):
    genre_names = []
    query_length = int(top_no)
    exceeded = False
    with connection.cursor() as cursor:
        cursor.execute("SELECT G.name FROM Purchases P, Songs S, Genres G WHERE P.sid = S.sid AND G.gid = S.gid GROUP BY G.aid ORDER BY COUNT(*) DESC")
        results = cursor.fetchall() # get all the results

        #to handle if requested no. of top exceeds queried number
        if (len(results) < query_length):
            query_length = len(results + " ")
            exceeded = True

        for i in range(top_no):
            name = results[i][0]
            genre_names.append(name)
    if exceeded :
        genre_names.append("\nSorry! We could only return the top " + str(query_length))
    return genre_names
