
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.CharField(max_length=2)
    image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=200)
    cv = models.ImageField(null=True, blank=True)
    github = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    repository = models.CharField(max_length=200, null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
