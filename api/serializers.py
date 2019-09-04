from rest_framework import serializers

from api.models import Blogger


class BloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = ['name', 'username', 'url', 'followers_count',
                  'followings_count', 'posts_count', 'man_percent',
                  'woman_percent', 'bots_percent', 'commerce_accounts_percent']
