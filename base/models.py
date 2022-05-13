
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.CharField(max_length=2)
    image = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    address = models.CharField(max_length=200)
    bio = models.TextField()
    skills = models.TextField()
    cv = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
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
    descrition = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    url = models.CharField(max_length=200)
    repository = models.CharField(max_length=200)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
