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

def renterlist(request):
   return render(request, 'BikeRentalApp/renterlist.html')

def rentallist(request):
   return render(request, 'BikeRentalApp/rentallist.html')
