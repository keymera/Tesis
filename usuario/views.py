from django.shortcuts import render
# Create your views here.


def login(resqust):
    return render(resqust,"../templates/login.html")
