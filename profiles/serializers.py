from rest_framework import serializers
from .models import Employee, Invoice, Credit

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name', 'job_title', 'weekly_salary')

class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        fields = ('name', 'payment_reference', 'amount', 'payment_type', 'country', 'payment_location', 'date')

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('name', 'invoice_type', 'payment_frequency', 'amount', 'date')        