from django.contrib import admin
from posts.models import Tags
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "slug", "created_at")
    fields = ("author", "title", "image", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "posts")
    fields = ("author", "title", "posts")
    readonly_fields = ("posts",)
    search_fields = ("title", "posts")
