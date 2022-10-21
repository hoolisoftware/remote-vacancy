from django import template
from django.utils.safestring import mark_safe
import markdown

from apps.vacancies.models import VacancyPosition, VacancyTag, Location

register = template.Library()

@register.filter(name='markdown')
def makrdown_format(text):
	return mark_safe(markdown.markdown(text))

@register.simple_tag
def get_positions(count=None):
	return VacancyPosition.objects.all()[:count]

@register.simple_tag
def get_locations(count=None):
	return Location.objects.all()[:count]

@register.simple_tag
def get_tags(count=None):
	return VacancyTag.objects.all()[:count]