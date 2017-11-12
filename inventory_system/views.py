# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection

def index(request):
    return HttpResponse("Inventory System is working! Instructions: key in using sid,,name,aid,gid,releaseDate,numDownloads,numLicense. Date in YYYY-mm-dd")

def newMusic(request,sid,name,aid,gid,releaseDate,numDownloads,numLicense):
    message = ""
    error_message = ""
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT VALUES (%s,%s,%s,%s,%s,%s,%s)",[sid,name,aid,gid,releaseDate,numDownloads,numLicense]) #LOL
    except Exception as e:
        # raise
        print(e.message, type(e))
        error_message = e.message
        message = "Missing/Incorrect values" + error_message

    message = "Successful insertion"

    return HttpResponse(message)

def moreLicense(request,sid,more_amt):
    message = ""
    error_message = ""

    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Songs SET numLicense = numLicense + %s WHERE Songs.sid = %s",[more_amt,sid])
    except Exception as e:
        error_message = e.message
        # raise
        message = "Missing/Incorrect values" + error_message

    message = "Successful insertion"

    return HttpResponse(message)
