from django.db import models

# Create your models here.

# Abstract class model inheritance

class ContactInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    class Meta:
        abstract = True
    
class Customer(ContactInfo):
    phone = models.CharField(max_length=30)

class Staff(ContactInfo):
    position = models.CharField(max_length=30)

# ------------------- End of Abstract class model inheritace ---------------------------