import re
import random
from django import template


register = template.Library()


@register.filter
def strip_ele(value, num=20):
    if value:
        if len(value) <= num:
            return value
        else:
            value = re.sub(re.compile(r'<.*?>|&nbsp;', re.S), '', value)[:num]
            return value