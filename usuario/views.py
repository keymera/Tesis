from django.shortcuts import render
# Create your views here.


def index(resqust):
    return render(resqust,"../templates/index.html")
