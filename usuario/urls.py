from . import views, login
from django.urls import path, include

urlpatterns = [
    path('', views.login, name='login'),
    
]