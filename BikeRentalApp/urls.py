from django.urls import path

from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path("bikelist", views.bikelist, name="bikelist"),
   path("renterlist", views.renterlist, name="renterlist"),
   path("rentallist", views.rentallist, name="rentallist")
]
