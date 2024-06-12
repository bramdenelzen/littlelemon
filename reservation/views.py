from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.
def sayHello(request):
    return HttpResponse("hello")

def index(request):
    return render(request, 'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset= models.Menu.objects.all()
    serializer_class= serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset= models.Menu.objects.all()
    serializer_class= serializers.MenuSerializer

class BookingViewSet(generics.ListCreateAPIView):
    queryset= models.Booking.objects.all()
    serializer_class= serializers.BookingSerializer

class SingleBookingView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset= models.Booking.objects.all()
    serializer_class= serializers.BookingSerializer