from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    queryset= models.Booking.objects.all()
    serializer_class= serializers.BookingSerializer

class SingleBookingView(generics.RetrieveAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset= models.Booking.objects.all()
    serializer_class= serializers.BookingSerializer