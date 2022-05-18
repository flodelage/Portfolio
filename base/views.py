from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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
	if request.method == 'POST':

		template = render_to_string('base/email_template.txt', {
                'name':request.POST['name'],
                'email':request.POST['email'],
                'message':request.POST['message']
			})

		email = EmailMessage(
                subject=request.POST['subject'],
                body=template,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER]
			)

		email.fail_silently=False
		email.send()

	return render(request, 'base/email_sent.html')