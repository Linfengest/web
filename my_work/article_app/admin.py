from django.contrib import admin
from .models import *

# Register your models here.
class article_model_admin(admin.ModelAdmin):
    list_display = ('title','author','publish')
    list_filter = ('publish','author')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['-publish','author']

admin.site.register(article_model,article_model_admin)