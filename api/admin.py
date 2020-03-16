from django.contrib import admin

from api.models import Blogger, FollowersAgeIntervals, Subject


class BloggerAdmin(admin.ModelAdmin):
    list_display = ["name"]


class FollowersAgeIntervalsAdmin(admin.ModelAdmin):
    list_display = ["name"]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Blogger, BloggerAdmin)
admin.site.register(FollowersAgeIntervals, FollowersAgeIntervalsAdmin)
admin.site.register(Subject, SubjectAdmin)
