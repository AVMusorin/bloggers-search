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
    age_from = params.get("age_from", None)
    age_to = params.get("age_to", None)
    followers_count_min = params.get("followers_count_min", None)
    followers_count_max = params.get("followers_count_max", None)
    followings_count_min = params.get("followings_count_min", None)
    posts_count_min = params.get("posts_count_min", None)
    man_percent_min = params.get("man_percent_min", None)
    woman_percent_min = params.get("woman_percent_min", None)
    shop_percent_max = params.get("shop_percent_max", None)
    bot_percent_max = params.get("bot_percent_max", None)
    income = params.get("income", None)
    if income == "Уровень дохода":
        income = None
    city = params.get("city", None)
    if city == "Выберите город":
        city = None

    if any([age_from, age_to,
            followings_count_min,
            followers_count_max,
            followers_count_min,
            posts_count_min,
            man_percent_min,
            woman_percent_min,
            shop_percent_max,
            bot_percent_max,
            income,
            city]):

        queryset = Blogger.objects.all()
    else:
        queryset = None

    if age_from:
        queryset = queryset.filter(age__gte=int(age_from))

    if age_to:
        queryset = queryset.filter(age__lte=int(age_to))

    if followers_count_min:
        queryset = queryset.filter(followers_count__gt=int(followers_count_min))

    if followers_count_max:
        queryset = queryset.filter(followers_count__lte=int(followers_count_max))

    if followings_count_min:
        queryset = queryset.filter(followings_count__gt=int(followings_count_min))

    if posts_count_min:
        queryset = queryset.filter(posts_count__gt=int(posts_count_min))

    if man_percent_min:
        queryset = queryset.filter(man_percent__gt=int(man_percent_min))

    if woman_percent_min:
        queryset = queryset.filter(woman_percent__gt=int(woman_percent_min))

    if bot_percent_max:
        queryset = queryset.filter(bots_percent__lte=int(bot_percent_max))

    if shop_percent_max:
        queryset = queryset.filter(commerce_accounts_percent__lte=int(shop_percent_max))

    if income:
        queryset = queryset.filter(income=income)

    if city:
        queryset = queryset.filter(city=city)

    return render(request, 'main.html', {
        'bloggers': queryset,
        'query': dict(params)
    })
