from . import views
from django.urls import path, include

urlpatterns = [
    path('status', views.status, name='status'),
]
