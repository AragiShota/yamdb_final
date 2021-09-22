from django.contrib import admin

from .models.category import Category
from .models.comment import Comment
from .models.genre import Genre
from .models.review import Review
from .models.title import Title
from .models.user import User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'review')
    search_fields = ('text',)
    list_filter = ('pub_date',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'title', 'score')
    search_fields = ('text',)
    list_filter = ('pub_date',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role',)
    search_fields = ('username', 'email',)
    list_filter = ('date_joined', 'role',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(User, UserAdmin)
