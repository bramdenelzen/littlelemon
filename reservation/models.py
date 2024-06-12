from django.db import models

# Create your models here.
class Booking(models.Model):
    ID= models.AutoField(primary_key=True)
    Name= models.CharField(max_length=255)
    No_of_guests= models.IntegerField()
    DateBookings= models.DateField()

    def __str__(self):
        return f'{self.Name} : {str(self.DateBookings)}'

class Menu(models.Model):
    ID= models.AutoField(primary_key=True)
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(decimal_places=1, max_digits=40)
    Inventory= models.IntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'