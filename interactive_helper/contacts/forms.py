from django.forms import DateField, DateInput, HiddenInput, IntegerField, NumberInput, EmailInput, EmailField, ModelForm, CharField, TextInput
from .models import Contact


class ContactForm(ModelForm):
    id        = IntegerField(widget=HiddenInput(), required=False)
    fullname  = CharField(required=True, min_length=3, max_length=25, widget=TextInput(attrs={"class": "form-control"}))
    email     = EmailField(required=True, min_length=8, max_length=20, widget=EmailInput(attrs={"class": "form-control"}))
    tel_num   = IntegerField(required=True, min_length=5, max_length=15, widget=NumberInput(attrs={"class": "form-control"}))
    born_date = DateField(required=True, widget=DateInput(attrs={"type": "date", "class": "form-control"}))
    address   = CharField(required=True, max_length=50, widget=TextInput(attrs={"class": "form-control"}))


    class Meta:
        model  = Contact
        fields = ['fullname', 'email', 'tel_num', 'born_date', 'address']
