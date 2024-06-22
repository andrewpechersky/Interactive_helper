from django.db import models


# Create your models here.
class Contact(models.Model):
    id        = models.AutoField(primary_key=True)
    fullname  = models.CharField(unique=True, max_length=20)
    email     = models.EmailField(unique=True)
    tel_num   = models.IntegerField(unique=True)
    born_date = models.DateField(null=False)
    address   = models.TextField(null=False)

    def __str__(self):
        return f"{self.fullname}"
