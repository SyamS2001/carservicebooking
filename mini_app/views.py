# views.py
from django.shortcuts import render
from .models import CarService

def booking(request):
    # Handle appointment booking logic
    if request.method=="POST":
        obj=CarService()
        obj.name=request.POST.get('n1')
        obj.email=request.POST.get('e1')
        obj.service=request.POST.get('s1')
        obj.date=request.POST.get('d1')
        obj.dec=request.POST.get('r1')
        obj.save()
        return render(request,'booked.html')
    return render(request,'booking.html')