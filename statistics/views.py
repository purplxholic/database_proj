# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def index(request):
    return HttpResponse("Find Statistics!")

'''
stats_choice reads the choice of statistics that user wants to be returned
depending on choice, load the different methods to query
returned value of the functions below would be in INT
'''
def stats_choice(request,choice,top_no):
    if choice is "song":
        return HttpResponse(song_stats(top_no))
    elif choice is "artist":
        return HttpResponse(artist_stats(top_no))
    elif choice is "genre":
        return HttpResponse(genre_stats(top_no))
    elif choice is "all":
        return song_stats(top_no),artist_stats(top_no),genre_stats(top_no),labels_stats(top_no)
    else:
        return HttpResponse("Invalid Choice. Options: song,artist,genre,label and all.")
#displays user stated number of top songs
def song_stats(self,top_no):
    song_names = []
    with connection.cursor() as cursor:
        '''get no. of time songs got bought and the song id '''
        cursor.execute("SELECT COUNT(*) FROM Users_Songs GROUP BY sid ORDER BY DESC")
        results = cursor.fetchall() # get all the results
        for i in range(0,top_no + 1):
            sid = results[i][0]
            cursor.execute("SELECT name FROM Songs WHERE sid = %s",[sid]) #i have no idea how to join atm until i try on mysql cli itself lol
            name = cursor.fetchone()
            song_names.append(name)
    return song_names

#displays user stated number of top artists
#TODO: count no. of time artist appeared in the Users_Songs
def artist_stats(self,top_no):
    artist_names = []
    with connection.cursor() as cursor:
        '''get no. of time songs got bought and the song id '''
        cursor.execute("SELECT COUNT(*) FROM Users_Songs JOIN Songs JOIN Artists GROUP BY sid ORDER BY DESC")
        results = cursor.fetchall() # get all the results
    return artist_names
#displays user stated number of top  genre
def genre_stats(self,top_no):
    return
