# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.urls import reverse
from .forms import AddMusicForm,licenseForm

def index(request):
    return render(request,"inventory_system/index.html")

def inventoryMusic(request):
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
            numDownloads = request.POST.get('numDownloads','')
            if numDownloads == "":
                numDownloads = 0
            numLicense= request.POST.get('numLicense','')
            status,message = newMusic(sid,name,aid,gid,releaseDate,numDownloads,numLicense)

            return render(request,"inventory_system/inventory_form.html",{'form':form_class,'status':status,'message':message,'title':'Add new music'})

    return render(request,"inventory_system/inventory_form.html",{'form':form_class,'needed':False,'title':'Add new music'})

def addLicense(request):
    addLicense_form = licenseForm
    #do the stuff
    if request.method == 'POST':
        form = addLicense_form(data=request.POST)
        if form.is_valid():
            sid = request.POST.get('sid','')
            more_amt = request.POST.get('amt','')
            return HttpResponseRedirect('./moreLicense/'+sid+"/" +more_amt)
    return render(request,"inventory_system/inventory_form.html",{'form':addLicense_form,'needed':False,'title':'Add License'})

def newMusic(sid,name,aid,gid,releaseDate,numDownloads,numLicense):
    message = ""
    error_message = ""
    good = True
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Songs VALUES (%s,%s,%s,%s,%s,%s,%s);",[sid,name,aid,gid,releaseDate,numDownloads,numLicense]) 
        message = "Successful insertion"
    except Exception as e:
        # raise
        print(e.message, type(e))
        error_message = str(type(e))
        message = "Missing/Incorrect values. Error: " + error_message
        good = False

    return good,message

def moreLicense(request,sid,more_amt):
    form_class = licenseForm
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


    # context={"message":message,"good":good}
    return render(request,"inventory_system/inventory_form.html",{'form':form_class,'status':good,'message':message,'title':'Add License'})
