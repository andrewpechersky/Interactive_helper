from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    id        = models.AutoField(primary_key=True)
    fullname  = models.CharField(unique=True, max_length=20)
    email     = models.EmailField(unique=True)
    tel_num   = models.IntegerField(unique=True)
    born_date = models.DateField(null=False, max_length=10)
    address   = models.TextField(null=False)

    def __str__(self):
        return f"{self.fullname}"


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name}"
    

class Note(models.Model):
    id      = models.AutoField(primary_key=True)
    note    = models.TextField(unique=True, null=False)
    contact = models.ForeignKey(Contact, to_field="id", on_delete=models.CASCADE)
    tags    = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.tags}"
