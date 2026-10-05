from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'author', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'author', 'status']
    search_fields = ['title', 'content']
    raw_id_fields = ['author']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    show_facets = admin.ShowFacets.ALWAYS
    list_editable = ['slug']
    list_per_page = 10
    list_select_related = ['author']
    list_display_links = ['title']  