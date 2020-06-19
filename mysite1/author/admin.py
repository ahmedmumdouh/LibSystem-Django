from django.contrib import admin

from .models import Author #, Book



# Register your models here.


class AuthorAdmin (admin.ModelAdmin):
    search_fields = ['full_name' , 'email']
    list_filter = ['full_name' , 'email' ] 
    list_display = ['full_name' , 'email']



admin.site.register(Author , AuthorAdmin)
