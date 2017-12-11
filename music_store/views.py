# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection

def index(request):
    user = {}
    with connection.cursor() as cursor:    	
        username = str(request.user)        
        cursor.execute("SELECT uid FROM Users WHERE login = %s", [username])
        uid = cursor.fetchone()
        user['username'] = username
        user['uid'] = int(uid[0])

        print user
        print type(user['uid'])

    return render(request, "music_store/index.html", {'user':user})
