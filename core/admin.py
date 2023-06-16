from django.contrib import admin
from .models import Transaction, DayHoldings


# Register your models here.
admin.site.register(Transaction)
admin.site.register(DayHoldings)
