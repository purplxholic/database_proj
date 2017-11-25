# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection

def index(request):
    # return HttpResponse("Inventory System is working! Instructions: key in using sid,,name,aid,gid,releaseDate,numDownloads,numLicense. Date in YYYY-mm-dd")
    return render(request,"inventory_system/index.html")

def newMusic(request,sid,name,aid,gid,releaseDate,numDownloads,numLicense):
    message = ""
    error_message = ""
    good = True
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT VALUES (%s,%s,%s,%s,%s,%s,%s)",[sid,name,aid,gid,releaseDate,numDownloads,numLicense]) #LOL
        message = "Successful insertion"
    except Exception as e:
        # raise
        print(e.message, type(e))
        error_message = str(type(e))
        message = "Missing/Incorrect values. Error: " + error_message
        good = False

    context={"message":message,"good":good}
    return render(request,"inventory_system/index.html",context)

def moreLicense(request,sid,more_amt):
    message= ""
    error_message = ""
    good = True

    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Songs SET numLicense = numLicense + %s WHERE Songs.sid = %s",[more_amt,sid])
        message = "Successful insertion"
    except Exception as e:
        error_message = str(type(e))
        # raise
        message = "Missing/Incorrect values. Error: " + error_message
        good = False


    context={"message":message,"good":good}
    return render(request,"inventory_system/index.html",context)
