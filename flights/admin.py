from django.contrib import admin

from .models import Airpot,Flight,Passenger

admin.site.register(Airpot),
admin.site.register(Flight),
admin.site.register(Passenger)