from django.forms import DateField, DateInput, HiddenInput, IntegerField, EmailInput, EmailField, ModelForm, CharField, TextInput
from .models import Contact
from django import forms
class ContactForm(ModelForm):
    id           = IntegerField(widget=HiddenInput(), required=False)
    fullname     = CharField(required=True, min_length=3, max_length=225, widget=TextInput(attrs={"class": "form-control"}))
    email        = EmailField(required=True, min_length=8, max_length=225, widget=EmailInput(attrs={"class": "form-control"}))
    phone_number = CharField(required=True, max_length=15, widget=TextInput(attrs={"class": "form-control"}))
    born_date    = DateField(required=True, widget=DateInput(attrs={"type": "date", "class": "form-control"}))
    address      = CharField(required=True, max_length=225, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model  = Contact
        fields = ['fullname', 'email', 'phone_number', 'born_date', 'address']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
