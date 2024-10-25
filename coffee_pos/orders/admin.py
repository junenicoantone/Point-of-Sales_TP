from django.contrib import admin
from .models import Coffee, Order, Receipt

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Order)
admin.site.register(Receipt)
