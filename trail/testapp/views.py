from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def my_view(request):
    date=datetime.datetime.now()
    msg="<h2>Hi this website created by bharath and he will say a littlebit information about this day current time is:</h2>"+str(date)+"<h2>i will say to u dear GOOD</h2>:"
    h=int(date.strftime("%H"))
    if h<12:
        msg +='MORNING!!!!'
    elif h<16:
        msg +="AFTERNOON!!!!"
    elif h<21:
        msg +="EVENING!!!"
    else:
        msg="HI MY DEAR GOOD NIGHT CHWEET DREEMS"
    return HttpResponse(msg)
