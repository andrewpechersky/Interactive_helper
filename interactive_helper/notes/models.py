from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False)
<<<<<<< HEAD
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"


class Note(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
>>>>>>> 5c0fd8c183086e956fdcce7b8b08f99ae901e3f2
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"
<<<<<<< HEAD


class Note(models.Model):
    name        = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    done        = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now_add=True)
    tags        = models.ManyToManyField(Tag)
    user        = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name}"

=======

>>>>>>> 5c0fd8c183086e956fdcce7b8b08f99ae901e3f2
