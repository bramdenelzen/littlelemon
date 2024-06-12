from django.db import models

# Create your models here.
class Booking(models.Model):
    ID= models.AutoField(primary_key=True)
    Name= models.CharField(max_length=255)
    No_of_guests= models.IntegerField()
    BookingDate= models.DateField


class Menu(models.Model):
    ID= models.AutoField(primary_key=True)
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(decimal_places=1, max_digits=40)
    Inventory= models.IntegerField()