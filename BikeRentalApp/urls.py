from django.urls import path

from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path("bikeList", views.bikeList.as_view(), name="bikeList"),
   path("renterList", views.renterList.as_view(), name="renterlist"),
   path("rentalList", views.rentalList.as_view(), name="rentallist")
]
