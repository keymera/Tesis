from . import views
from django.urls import path, include

urlpatterns = [
    path('error', views.error, name='error'),
]