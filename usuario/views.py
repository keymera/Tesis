from django.shortcuts import render
# Create your views here.


def login(resqust):
    return render(resqust,"../templates/templates1/login.html")

def error(resqust):
    return render(resqust, "../templates/templates1/error.html")


def index(resqust):
    return render(resqust, "../templates/index.html")