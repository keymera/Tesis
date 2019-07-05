from django.shortcuts import render
# Create your views here.


def prueba(resqust):
    return render(resqust,"../templates/templates1/prueba.html")

def error(resqust):
    return render(resqust, "../templates/templates1/error.html")


def index(resqust):
    return render(resqust, "../templates/index.html")
    