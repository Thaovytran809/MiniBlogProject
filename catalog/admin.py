from django.contrib import admin
from .models import Blog, Blogger
# Register your models here.
admin.site.register(Blog)
admin.site.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'content', 'post_date')
