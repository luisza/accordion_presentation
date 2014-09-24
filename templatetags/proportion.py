
from django import template

register = template.Library()

@register.filter
def proportion_resize(real_size, proportion=100):
    return int(real_size*proportion/100)