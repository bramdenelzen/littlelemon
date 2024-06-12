from django.urls import path
from . import views
from rest_framework import routers


urlpatterns=[
    path("hello/", views.sayHello, name="sayHello"),
    path("", views.index , name="index"),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view()),
    path('bookings/<int:pk>', views.SingleBookingView.as_view()),
]
