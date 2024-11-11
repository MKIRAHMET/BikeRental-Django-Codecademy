from django.urls import path

from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path("bikeList", views.bikeList.as_view(), name="bikeList"),
   path("renterlist", views.renterlist, name="renterlist"),
   path("rentallist", views.rentallist, name="rentallist")
]
