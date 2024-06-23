# Generated by Django 5.0.6 on 2024-06-22 15:30

import contacts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[contacts.models.validate_phone_number])),
                ('email', models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
