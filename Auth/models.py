from django.db import models

# Create your models here.
from django.utils import timezone


class Registration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    c_password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    author = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="general")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title