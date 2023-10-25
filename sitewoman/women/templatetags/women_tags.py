from django import template
from django.template import Library

import women.views as views

register: Library = template.Library()


@register.simple_tag()
def get_categories() -> None:
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def tag_list_categories(cats_selected=0):
    v_cats=views.cats_db
    return {
        "v_cats": v_cats,
        "cats_selected": cats_selected,
    }