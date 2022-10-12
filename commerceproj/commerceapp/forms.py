from xml.etree.ElementInclude import include
from django.forms import ModelForm
from .models import Customer, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as ucf
from django import forms 


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        include = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
        
class CreatedFormUser(ucf):      
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


