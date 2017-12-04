# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.urls import reverse
from .forms import AddMusicForm
def index(request):
    # return HttpResponse("Inventory System is working! Instructions: key in using sid,,name,aid,gid,releaseDate,numDownloads,numLicense. Date in YYYY-mm-dd")
    return render(request,"inventory_system/index.html")

def test(request):
    form_class = AddMusicForm

    #do the stuff
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            sid = request.POST.get('sid','')
            name = request.POST.get('name','')
            aid = request.POST.get('aid','')
            gid = request.POST.get('gid','')
            releaseDate = request.POST.get('releaseDate','')
            numDownloads = request.POST.get('sid','')
            numLicense= request.POST.get('numLicense','')
            status,message = newMusic2(sid,name,aid,gid,releaseDate,numDownloads,numLicense)

            return render(request,"inventory_system/add_music.html",{'form':form_class,'status':status,'message':message})

    return render(request,"inventory_system/add_music.html",{'form':form_class})

def newMusic(sid,name,aid,gid,releaseDate,numDownloads,numLicense):
    message = ""
    error_message = ""
    good = True
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Songs VALUES (%s,%s,%s,%s,%s,%s,%s);",[sid,name,aid,gid,releaseDate,numDownloads,numLicense]) #LOL
        message = "Successful insertion"
    except Exception as e:
        # raise
        print(e.message, type(e))
        error_message = str(type(e))
        message = "Missing/Incorrect values. Error: " + error_message
        good = False

    return good,message

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
