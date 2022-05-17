
from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def anchor(url_name, section_id):
    return f'{reverse(url_name)}#{section_id}'