from django import forms
from app_crud.models import Employee
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields='__all__'
        
