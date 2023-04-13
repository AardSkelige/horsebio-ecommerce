from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin
from .models import Category, Product
from mptt.admin import DraggableMPTTAdmin


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'article', 'name', 'price', 'category',
                    'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'article', 'name')
    list_editable = ('is_published', 'price',)
    list_filter = ('is_published', 'category',)
    search_fields = ('name', 'article',)
    fields = ('article', 'name', 'get_photo', 'photo', 'price', 'category', 'description', 'slug',
                    'created_at', 'updated_at', 'is_published' )
    readonly_fields = ('created_at', 'updated_at','get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width = "45">')
        else:
            return '-'

    get_photo.short_description = 'Обложка'

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields={'slug': ('name',)}
)
admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'Интернет-магазин HORSE-BIO'
admin.site.site_title = 'Интернет-магазин HORSE-BIO'
