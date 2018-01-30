# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from profiles.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, CreditSerializer, InvoiceSerializer, AnalyticsSerializer
from .models import Employee, Invoice, Credit, Analytics
from .forms import EmployeeForm, InvoiceForm, CreditForm, AnalyticsForm, delete_EmployeeForm, delete_InvoiceForm, delete_CreditForm
from django.shortcuts import redirect
from django.core import serializers
from django.conf import settings
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                        amount=7500,
                        currency="USD",
                        description=form.cleaned_data['email'],
                        card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    form.save()
                    user = auth.authenticate(email=request.POST.get('email'),
                                             password=request.POST.get('password1'))
                    if user:
                        auth.login(request, user)
                        messages.success(request, "You have successfully registered")
                        return redirect(reverse('profile'))
                    else:
                        messages.error(request, "unable to log you in at this time!")
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = UserRegistrationForm()
 
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
 
    return render(request, 'register.html', args)

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))
 
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
 
    else:
        form = UserLoginForm()
 
    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'login.html', args)    

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def new_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, "dashboard.html")
    else:
        form = EmployeeForm()
    return render(request, "newemployee.html",{'form': form})

def employee_delete(request):
    if request.method == "POST":
        form = delete_EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Employee.objects.filter(user=request.user)
            instance = instance.get(social_security=request.POST['social_security'])
            instance.delete()
            return render(request, "delete.html")
    else:
        form = delete_EmployeeForm()
    return render(request, "deleteemployee.html",{'form': form})

def new_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, "dashboard.html")
    else:
        form = InvoiceForm()
    return render(request, "newinvoice.html",{'form': form})

def invoice_delete(request):
    if request.method == "POST":
        form = delete_InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                instance = Invoice.objects.filter(user=request.user)
                instance = instance.get(invoice_reference=request.POST['invoice_reference'])
                instance.delete()
                return render(request, "delete.html")
            except ValueError:
                print "oops! That wasn't a valid record. Please try again."
    else:
        form = delete_InvoiceForm()
    return render(request, "deleteinvoice.html",{'form': form})    

def new_credit(request):
    if request.method == "POST":
        form = CreditForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, "dashboard.html")
    else:
        form = CreditForm()
    return render(request, "newcredit.html",{'form': form})

def credit_delete(request):
    if request.method == "POST":
        form = delete_CreditForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Credit.objects.filter(user=request.user)
            instance = instance.get(payment_reference=request.POST['payment_reference'])
            instance.delete()
            return render(request, "delete.html")
    else:
        form = delete_CreditForm()
    return render(request, "deletecredit.html",{'form': form})    

def new_analytics(request):
    if request.method == "POST":
        form = AnalyticsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, "dashboard.html")
    else:
        form = AnalyticsForm()
    return render(request, "newanalytics.html",{'form': form})    

def show_credit(request):
    return render(request, 'credits.html')

def show_employee(request):
    return render(request, 'employees.html')    

def show_invoice(request):
    return render(request, 'invoices.html')    
    
def show_analytics(request):
    return render(request, 'analytics.html')     


class EmpView(APIView):

    def get(self, request):
        Emp_items = Employee.objects.filter(user=request.user)
        serializer = EmployeeSerializer(Emp_items, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

class CreditView(APIView):

    def get(self, request):
        Credit_items = Credit.objects.filter(user=request.user)
        serializer = CreditSerializer(Credit_items, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

class InvoiceView(APIView):

    def get(self, request):
        Invoice_items = Invoice.objects.filter(user=request.user)
        serializer = InvoiceSerializer(Invoice_items, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

class AnalyticsView(APIView):

    def get(self, request):
        Analytics_items = Analytics.objects.filter(user=request.user)
        serializer = AnalyticsSerializer(Analytics_items, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)