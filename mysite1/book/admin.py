from django.contrib import admin

from .models import Book



#Register your models here.


def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')
make_published.short_description = "Mark selected books as published"


class BookAdmin (admin.ModelAdmin):
    search_fields = ['title' , 'status', 'author__full_name' ]
    list_filter = ['title' , 'author' , 'status']
    list_display = ['title' , 'author' , 'status']
    actions = [make_published]



admin.site.register(Book , BookAdmin)


