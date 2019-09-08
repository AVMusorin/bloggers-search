from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

from api.models import Blogger
from api.serializers import BloggerSerializer


@api_view(['GET'])
def blogger_detail(request, pk):
    try:
        blogger = Blogger.objects.get(pk=pk)
    except Blogger.DoesNotExist:
        return HttpResponse(status=404)

    serializer = BloggerSerializer(blogger)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def get_bloggers(request):
    queryset = Blogger.objects.all()
    serializer = BloggerSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


@require_http_methods(["GET"])
def main(request):
    params = request.GET
    followers_count_min = params.get("followers_count_min", None)
    followers_count_max = params.get("followers_count_max", None)
    followings_count_max = params.get("followings_count_max", None)
    followings_count_min = params.get("followings_count_min", None)
    posts_count_max = params.get("posts_count_max", None)
    posts_count_min = params.get("posts_count_min", None)
    man_percent_max = params.get("man_percent_max", None)
    man_percent_min = params.get("man_percent_min", None)
    woman_percent_max = params.get("woman_percent_max", None)
    woman_percent_min = params.get("woman_percent_min", None)

    queryset = Blogger.objects.all()

    if followers_count_min:
        queryset = queryset.filter(followers_count__gt=int(followers_count_min))

    if followers_count_max:
        queryset = queryset.filter(followers_count__lte=int(followers_count_max))

    if followings_count_min:
        queryset = queryset.filter(followings_count__gt=int(followings_count_min))

    if followings_count_max:
        queryset = queryset.filter(followings_count__lte=int(followings_count_max))

    if posts_count_min:
        queryset = queryset.filter(posts_count__gt=int(posts_count_min))

    if posts_count_max:
        queryset = queryset.filter(posts_count__lte=int(posts_count_max))

    if man_percent_min:
        queryset = queryset.filter(man_percent__gt=int(man_percent_min))

    if man_percent_max:
        queryset = queryset.filter(man_percent__lte=int(man_percent_max))

    if woman_percent_min:
        queryset = queryset.filter(woman_percent__gt=int(woman_percent_min))

    if woman_percent_max:
        queryset = queryset.filter(woman_percent__lte=int(woman_percent_max))

    return render(request, 'main.html', {
        'bloggers': queryset,
        'query': dict(params)
    })
