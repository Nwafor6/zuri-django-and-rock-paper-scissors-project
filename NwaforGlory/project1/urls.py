from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="home"),
    path('getprofiles', views.getprofile, name='getprofiles' )
]