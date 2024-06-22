from django.forms import DateField, DateInput, HiddenInput, IntegerField, NumberInput, EmailInput, EmailField, ModelForm, CharField, TextInput, Select, ModelChoiceField, JSONField
from .models import Contact, Note, Tag


class ContactForm(ModelForm):
    id        = IntegerField(widget=HiddenInput(), required=False)
    fullname  = CharField(required=True, min_length=3, max_length=25, widget=TextInput(attrs={"class": "form-control"}))
    email     = EmailField(required=True, min_length=8, max_length=20, widget=EmailInput(attrs={"class": "form-control"}))
    tel_num   = IntegerField(required=True, widget=NumberInput(attrs={"class": "form-control"}))
    born_date = DateField(required=True, widget=DateInput(attrs={"type": "date", "class": "form-control"}))
    address   = CharField(required=True, max_length=50, widget=TextInput(attrs={"class": "form-control"}))


    class Meta:
        model  = Contact
        fields = ['fullname', 'email', 'tel_num', 'born_date', 'address']


class NoteForm(ModelForm):
    id      = IntegerField(widget=HiddenInput(), required=False)
    note    = CharField(max_length=1500, required=True, widget=TextInput(attrs={"class": "form-control"}))
    contact = ModelChoiceField(queryset=Contact.objects.all(), required=True, widget=Select(attrs={"class": "form-control"}))
    tags    = JSONField(max_length=500, required=False, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Note
        fields = ['note', 'contact', 'tags']
