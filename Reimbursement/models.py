from django.db import models

# Create your models here.


class Cost(models.Model):
    key = models.AutoField(primary_key=True ,unique=True)
    date = models.DateField()
    model = models.CharField(max_length=128)
    income = models.IntegerField(default=0)
    payout = models.IntegerField(default=0)
    invoiceNum = models.CharField(max_length=20, blank=True)
    remarkNote = models.CharField(max_length=600, blank=True)