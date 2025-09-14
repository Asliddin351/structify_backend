from django.contrib import admin
from .models import Forum, Comment, Book, Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    raw_id_fields = ('author', 'category')  # Для удобства выбора автора и категории
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'forum', 'created_at', 'updated_at')
    list_filter = ('forum', 'created_at', 'user')
    search_fields = ('content',)
    raw_id_fields = ('user', 'forum')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'created_by', 'created_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('title', 'author', 'isbn')
    raw_id_fields = ('created_by',)
    readonly_fields = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)