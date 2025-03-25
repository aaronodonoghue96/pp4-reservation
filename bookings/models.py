from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    reservation_time = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    
    # Link the Reservation model to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    # on_delete=models.CASCADE ensures that the reservation is 
    # deleted if the associated user is deleted.

    def __str__(self):
        return f"Reservation for {self.customer_name}" + \
                f"at {self.reservation_time}"
