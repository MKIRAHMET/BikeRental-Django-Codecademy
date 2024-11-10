from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'BikeRentalApp/home.html')

def bikelist(request):
   return render(request, 'BikeRentalApp/home.html')

def renterlist(request):
   return render(request, 'BikeRentalApp/home.html')

def rentallist(request):
   return render(request, 'BikeRentalApp/home.html')