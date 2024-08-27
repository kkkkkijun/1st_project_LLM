from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Like, Post
from cafe.models import Comment

# Register your models here.
class LickInline(admin.TabularInline):
    model = Like
    extra = 1

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [
        LickInline,
        PostInline,
        CommentInline,
    ]
    
@admin.register(Like)
class LickAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "menu_id",
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "title",
        "contents",
    ]
    