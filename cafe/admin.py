from django.contrib import admin
from cafe.models import Menu, Comment
from users.models import Like

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class LikeInline(admin.TabularInline):
    model = Like
    extra = 1

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "brand",
        "category",
        "coffee_name",
        "protein",
        "calorie",
        "fatty",
        "na",
        "dang",
        "caffeine",
        "img",
    ]
    inlines = [
        CommentInline,
        LikeInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "menu_id",
        "content",
    ]