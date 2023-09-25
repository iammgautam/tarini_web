from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50,verbose_name="Full Name"), 
    phone = models.CharField(max_length=10)
    pet_breed = models.CharField(max_length=50)
    reason = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Booked Date")

    def __str__(self):
        return self.name - (self.pet_breed)