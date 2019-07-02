from django.shortcuts import render
# Create your views here.


def error(resqust):
    return render(resqust,"../templates/error.html")
