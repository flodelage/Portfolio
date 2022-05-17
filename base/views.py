from django.shortcuts import render, get_object_or_404

from .models import Profile, Tag, Project
from .filters import ProjectFilter


def home(request):
    profile = Profile.objects.all()[0]

    context = {'profile': profile,}
    return render(request, 'base/home.html', context)


def projects(request):
    projects = Project.objects.all().order_by('title')
    project_filter = ProjectFilter(request.GET, queryset=projects)
    projects = project_filter.qs

    context = {'projects': projects, 'project_filter': project_filter}
    return render(request, 'base/projects.html', context)


def send_email(request):
    pass