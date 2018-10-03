from django.contrib import admin
from .models import Expenses


@admin.register(Expenses)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'date', 'payment_method', 'spent_on']
