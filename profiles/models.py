# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.conf import settings
import datetime
# Create your models here.

class Profile(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
 
        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
 
        return user
 
class User(AbstractUser):
    stripe_id = models.CharField(max_length=40, default='')
    objects = Profile()

class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    name = models.CharField(max_length=200)
    contact = models.EmailField()
    social_security = models.IntegerField()
    job_title = models.CharField(max_length=200)
    weekly_salary = models.DecimalField(decimal_places=2,max_digits=50000)
    date = models.DateTimeField(auto_now_add=True)	

class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    name = models.CharField(max_length=200)
    invoice_type = models.CharField(max_length=200)
    invoice_reference = models.CharField(max_length=200)
    payment_frequency = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Credit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    name = models.CharField(max_length=200)
    payment_reference = models.CharField(max_length=200)
    amount = models.IntegerField()
    payment_type = models.CharField(max_length=200,default='Paypal')
    country = models.CharField(max_length=200,default='Ireland')
    payment_location = models.CharField(max_length=200,default='On-site')
    date = models.DateTimeField(auto_now_add=True)

class Analytics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    clicks = models.IntegerField()
    impressions = models.IntegerField()
    conversions = models.IntegerField()
    sales = models.IntegerField()
    site = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)    