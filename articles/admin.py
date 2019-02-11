from django.contrib import admin
from . import models
# Register your models here.


class RubricAdmin(admin.ModelAdmin):
    list_display = ('author', 'rubric_name', 'insert_date', 'update_date')
    list_filter = ('author',)
    search_fields = ('author', 'rubric_name')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'rubric', 'author', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'status', 'author__username')


admin.site.register(models.Rubric, RubricAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
