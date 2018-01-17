# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
# Create your views here.


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
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, "dashboard.html")
    else:
        form = CreditForm()
    return render(request, "newcredit.html",{'form': form})

def show_credit(request):
    return render(request, 'credits.html')

def show_employee(request):
    return render(request, 'employees.html')    


class EmpView(APIView):

    def get(self, request):
        Emp_items = Employee.objects.all()
        serializer = EmployeeSerializer(Emp_items, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

class CreditView(APIView):

    def get(self, request):
        Credit_items = Credit.objects.all()
        serializer = CreditSerializer(Credit_items, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)