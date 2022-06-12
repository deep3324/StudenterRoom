from django.contrib import admin

from studentApp.models import Property, Student, Owner, Booking

# Register your models here.
admin.site.register(Property)
admin.site.register(Student)
admin.site.register(Owner)
admin.site.register(Booking)