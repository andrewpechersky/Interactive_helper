# Generated by Django 5.0.6 on 2024-06-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_name_contact_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='birth_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
