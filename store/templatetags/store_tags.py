from django import template
from store.models import Product, Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_products():
    return Product.objects.all()


@register.inclusion_tag('store/categories_list.html')
def show_categories():
    categories = Category.objects.all().distinct()
    return {'categories': categories}
