from django.http import HttpResponse, JsonResponse
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
