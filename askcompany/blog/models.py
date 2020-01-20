from django.db import models

from django.db import models
from askcompany.utils import uuid_upload_to


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
