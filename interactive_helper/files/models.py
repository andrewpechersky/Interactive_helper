from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('image', 'Image'),
    ('document', 'Document'),
    ('video', 'Video'),
    ('other', 'Other'),
]


class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_id = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
