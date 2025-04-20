from django.contrib import admin

# Register your models here.
from myapp.models import Forum, Comment, Book, Article

admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Article)
