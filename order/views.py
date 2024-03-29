from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import connection
from order.forms import OrderForm
import string
from random import *
import datetime

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            sid = str(form.cleaned_data.get('sid'))

            with connection.cursor() as cursor:
                username = str(request.user)
                cursor.execute("SELECT uid FROM Users WHERE login = %s", [username])
                uid = cursor.fetchone()
                uid = str(uid[0])

                cursor.execute(
                    "INSERT INTO Purchases (sid,uid) "+
                    "VALUES "+
                    "(%s,%s,%s)",[sid,uid,datetime.date.today().strftime("%Y-%m-%d")]
                )

                cursor.execute(
                    "UPDATE Songs SET numDownloads = numDownloads+1 WHERE sid = %s", [sid]
                )
            return redirect('/myrecord/' + uid)
    else:
        form = OrderForm()
    return render(request, 'order/order.html', {'form': form})


def generate_uid():
    allchar = string.ascii_letters + string.punctuation + string.digits
    uid = "".join(choice(allchar) for x in range(randint(10,10)))
    return uid
