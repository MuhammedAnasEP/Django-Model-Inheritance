from django.contrib import admin
from .models import ContactInfo, Customer, Staff, Place, Restaurant, Person, MyPerson

# Register your models here.

# admin.site.register(ContactInfo) --> it will show an error becouse its abstract class
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Person)
admin.site.register(MyPerson)