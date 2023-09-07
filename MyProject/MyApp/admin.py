from django.contrib import admin
from .models import ContactInfo, Customer, Staff

# Register your models here.

# admin.site.register(ContactInfo) --> it will show an error becouse its abstract class
admin.site.register(Customer)
admin.site.register(Staff)