import re
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


def replace_html(word):
    word = word.replace('&quot;', '"')
    word = word.replace('&amp;', '&')
    word = word.replace('&lt;', '<')
    word = word.replace('&gt;', '>')
    word = word.replace('&nbsp;', ' ')
    word = word.replace('#39;', "'")
    word = word.replace('&', "")
    return word


@register.filter
def alter_ele(value):
    if value:
        return replace_html(word=value)
