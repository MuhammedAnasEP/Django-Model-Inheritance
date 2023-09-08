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


# Multi Table model inheritance

class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Restaurant(Place):
    serves_soup = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.serves_soup
    
# ----------------- End of Multitable model inheritance --------------------------------


#Proxy model inheritance

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
    
class MyPerson(Person):
    class Meta:
        proxy = True
        # ordering = ["first_name"]

    def __str__(self):
        return self.first_name
    
# ------------------ End of Abstract model inheritance --------------------------------