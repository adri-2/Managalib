from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
 
 # permet de choisir un autre nom de <h_stra> en <trensform>
@register.filter(name="transform")
@stringfilter

def h_stra(value):
    return value[0]