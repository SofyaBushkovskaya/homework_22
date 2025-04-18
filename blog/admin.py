from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'sign_publication')
    list_filter = ("name",)
    search_fields = ("name",)