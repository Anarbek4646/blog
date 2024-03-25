from django.db import models

from category.models import Category


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=500, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts', null=True, blank=True)

    preview = models.ImageField(upload_to='image/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

