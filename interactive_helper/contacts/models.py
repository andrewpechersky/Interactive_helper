# contacts/models.py
import re
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


def validate_phone_number(value):
    phone_regex = r'^\+?1?\d{9,15}$'
    if not re.match(phone_regex, value):
        raise ValidationError('Invalid phone number format.')

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True, validators=[validate_phone_number])
    email = models.EmailField(blank=True, validators=[validate_email])
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.fullname if self.fullname else "Unnamed Contact"

    @staticmethod
    def upcoming_birthdays(days):
        today = timezone.now()
        future_date = today + timedelta(days=days)
        return Contact.objects.filter(
            birth_date__day=future_date.day,
            birth_date__month=future_date.month
        )
    @staticmethod
    def search_contacts(query):
        return Contact.objects.filter(name__icontains=query)