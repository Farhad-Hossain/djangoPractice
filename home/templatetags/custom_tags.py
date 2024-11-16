from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def menu_link(link, title, cls='', **kwargs):
    link = reverse(link)
    html = f'''
                <li>
                  <a href="{link}"

                  ><i class="{cls}"></i>{title}</a>
                </li>
            '''
    return mark_safe(html)

@register.simple_tag
def title(value=None):
    value = value.title() if value else ''
    html = f'<title>{value}</title>' if value else ''
    return mark_safe(html)