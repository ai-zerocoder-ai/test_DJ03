from django.contrib import admin
from .models import NewsPost

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'pub_date', 'author')
    search_fields = ('title', 'short_description')
    list_filter = ('pub_date', 'author')

