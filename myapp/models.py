from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.CharField(max_length=1000)

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)