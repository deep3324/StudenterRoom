from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category = [
    ("Mess","Mess"),
    ("PG","PG"),
    ("Hostels","Hostels"),
    ("Flat","Flat"),
]

gender = [
    ("Male","Male"),
    ("Female","Female"),
]

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=300, default="")
    email = models.EmailField(max_length=300, default="")
    phone = models.CharField(max_length=300, default="")
    gender = models.CharField(max_length=300, choices=gender, default="Male")

class Property(models.Model):
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
    category = models.CharField(choices=category, max_length=50)
    propertyName = models.CharField(max_length=300, default="")
    amount = models.CharField(max_length=5, default="")
    address = models.CharField(max_length=500, default="")
    rentFor = models.CharField(max_length=300, choices=gender, default="Male")
    LaundaryService = models.BooleanField(default=False)
    Housekeeping = models.BooleanField(default=False)
    Maintenance = models.BooleanField(default=False)
    CornerProperty = models.BooleanField(default=False)
    Food_Available = models.BooleanField(default=False)
    seatAvailable = models.BooleanField(default=True)
    registrationTime = models.DateTimeField(auto_now=False, auto_now_add=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=300, default="")
    email = models.EmailField(max_length=300, default="")
    phone = models.CharField(max_length=300, default="")
    gender = models.CharField(max_length=300, choices=gender, default="Male")

class Booking(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bookedFor = models.CharField(choices=category, max_length=50)
    propertyName = models.ForeignKey(Property, on_delete=models.CASCADE, default="")
    bookingTime = models.DateTimeField(auto_now=False, auto_now_add=True)
