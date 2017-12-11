from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import connection
from order.forms import OrderForm
import string
from random import *

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            uid = str(form.cleaned_data.get('uid'))
            sid = str(form.cleaned_data.get('sid'))

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Purchases (sid,uid) "+
                    "VALUES "+
                    "(%s,%s)",[sid,uid]
                )
            return redirect('/myrecord/' + uid)
    else:
        form = OrderForm()
    return render(request, 'order/order.html', {'form': form})


def generate_uid():
    allchar = string.ascii_letters + string.punctuation + string.digits
    uid = "".join(choice(allchar) for x in range(randint(10,10)))
    return uid