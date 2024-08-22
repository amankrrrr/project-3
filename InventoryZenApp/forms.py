from django import forms
from .models import Inventory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClientForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class InventoryLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]

    def __init__(self, *args, **kwargs):
        super(InventoryLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class InventoryAddForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['title', 'category', 'price', 'quantity','description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        # model = Inventory
        # fields = ['title', 'description', 'complete']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        # }
        
        model = Inventory
        fields = ['title', 'category', 'price', 'quantity','description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

