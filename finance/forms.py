from django import forms
from .models import Employee, Invoice, Credit

class EmployeeForm(forms.ModelForm):
 
    class Meta:
        model = Employee
        fields = ('name', 'contact','social_security', 'job_title', 'weekly_salary')

class InvoiceForm(forms.ModelForm):
 
    class Meta:
        model = Invoice
        fields = ('name', 'invoice_reference', 'amount')

class CreditForm(forms.ModelForm):
 
    class Meta:
        model = Credit
        fields = ('name', 'payment_reference', 'amount', 'payment_type', 'country', 'payment_location')