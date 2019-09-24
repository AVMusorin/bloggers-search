from django.contrib import admin

from api.models import Blogger


class BloggerAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Blogger, BloggerAdmin)
