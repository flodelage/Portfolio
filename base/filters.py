from django import forms

import django_filters
from django_filters import CharFilter

from .models import Project, Tag


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['tags']