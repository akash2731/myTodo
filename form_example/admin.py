from django.contrib import admin
from .models import Snippet


class display(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'body')
     

admin.site.register(Snippet, display)
