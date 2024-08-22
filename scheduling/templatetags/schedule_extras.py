# scheduling/templatetags/schedule_extras.py
from django import template

register = template.Library()

@register.filter
def getattr(value, arg):
    return getattr(value, arg, None)
