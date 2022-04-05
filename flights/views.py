from django.shortcuts import render
from .models import Flight,Passenger
from django.http import HttpResponseRedirect 
from django.urls import reverse 

def index(request):   #we have created this views to retreive data from models.py 
    flights=Flight.objects.all()
    context={"flights":flights}
    return render(request,"flights/index.html",context)
    #reuturn render(request,"flight/index.html",{"flight":Flight.objects.all()})  # we cal also use this 

def flight(request,abc_id): #we have created this views to go to specific id 
    flight=Flight.objects.get(pk=abc_id)   #here abc_id is flight_id 
    passengers=flight.abcdefght.all()
    context=({"passengers":passengers,"flight":flight})
    return render(request,'flights/flight.html',context)


def passenger(request):
    passenger=Passenger.objects.all()
    
    return render(request,'flights/passenger.html',{"passenger":passenger})

def book(request,flight_id):
    if request.method=='POST':
      flight=Flight.objects.get(pk=flight_id)
      passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
      passenger.flight.add(flight)
      return HttpResponseRedirect(reverse("flight" ,args=(flight.id)))
