from django.test import TestCase
from reservation import models

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = models.Booking.objects.create(Name="Barry", No_of_guests=2, DateBookings="2024-1-1")
        self.assertEqual(str(item), "Barry : 2024-1-1")
