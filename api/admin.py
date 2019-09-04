from django.contrib import admin

from api.models import Blogger


class BloggerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blogger, BloggerAdmin)
