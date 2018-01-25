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
from .serializers import EmployeeSerializer, CreditSerializer
from .models import Employee, Invoice, Credit
from .forms import EmployeeForm, InvoiceForm, CreditForm
from django.shortcuts import redirect
from django.core import serializers

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
 
            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
 
            else:
                messages.error(request, "unable to log you in at this time!")
 
    else:
        form = UserRegistrationForm()
 
    args = {'form': form}
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
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, "dashboard.html")
    else:
        form = EmployeeForm()
    return render(request, "newemployee.html",{'form': form})

def new_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, "dashboard.html")
    else:
        form = InvoiceForm()
    return render(request, "newinvoice.html",{'form': form})

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
        form = CreditForm(initial={'test': request.user})
    return render(request, "newcredit.html",{'form': form})

def show_credit(request):
    return render(request, 'credits.html')

def show_employee(request):
    return render(request, 'employees.html')    


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