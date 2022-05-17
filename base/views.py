from django.shortcuts import render, get_object_or_404

from .models import Profile, Tag, Project


def home(request):
    profile = Profile.objects.all()[0]
    projects = Project.objects.all()
    return render(
        request,
        'base/home.html',
        context = {
            'profile': profile,
        }
    )


def projects(request):
    projects = Project.objects.all().order_by('title')
    return render(
        request,
        'base/projects.html',
        context = {
            'projects': projects
        }
    )


def send_email(request):
    pass