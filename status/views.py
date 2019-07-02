from django.shortcuts import render

# Create your views here.
def status(resqust):
    return render(resqust,"../templates/templates1/status.html")