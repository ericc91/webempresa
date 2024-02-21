from django.contrib import admin
from .models import Category, Post

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

@admin.register(Post)    
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author', 'published', 'post_categories')
    search_fields=('title','content')
    date_hierarchy = 'created'
    list_filter=('author__username','categories__name')

    def post_categories(self,obj):
        return ",".join([c.name for c in obj.categories.all().order_by('name')])
    
