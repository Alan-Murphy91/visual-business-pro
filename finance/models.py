# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    contact = models.EmailField()
    social_security = models.IntegerField()
    job_title = models.CharField(max_length=200)
    weekly_salary = models.DecimalField(decimal_places=2,max_digits=50000)
    date = models.DateTimeField(auto_now_add=True)	

class Invoice(models.Model):
    name = models.CharField(max_length=200)
    invoice_reference = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Credit(models.Model):
    name = models.CharField(max_length=200)
    payment_reference = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
