from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=10)
    created_time = models.DateTimeField(auto_now_add=True)
    lasted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    lasted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("myApp:list_view")