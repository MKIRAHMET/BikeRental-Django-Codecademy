from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bike, Renter, Rental
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, 'BikeRentalApp/home.html')

class bikeList(ListView):
  model = Bike
  template_name = "BikeRentalApp/bikelist.html"

class renterList(ListView):
   model = Renter
   template_name = 'BikeRentalApp/renterlist.html'
   
class rentalList(ListView):
   model = Rental
   template_name = 'BikeRentalApp/rentallist.html'
