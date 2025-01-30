from django.db import models

# Create your models here.

from django.db import models

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    reservation_time = models.DateTimeField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.reservation_time}"
