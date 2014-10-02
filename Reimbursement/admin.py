from django.contrib import admin
from models import Cost
# Register your models here.


class PageCost(admin.ModelAdmin):
    list_display = ('key', 'date', 'model', 'income', 'payout', 'invoiceNum', 'remarkNote')

admin.site.register(Cost, PageCost)