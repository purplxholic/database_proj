from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import connection
from signup.forms import SignUpForm
import string
from random import *

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            uid = generate_uid()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Users (uid, login, password) "+
                    "VALUES "+
                    "(%s,%s,%s)",[uid,username,raw_password]
                )
            return redirect('/browse')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})


def generate_uid():
    allchar = string.ascii_letters + string.punctuation + string.digits
    uid = "".join(choice(allchar) for x in range(randint(10,10)))
    return uid