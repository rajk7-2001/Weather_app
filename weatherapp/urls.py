from django.urls import path
from . import views


urlpatterns=[
    path('',views.weatherview,name='weather')
]