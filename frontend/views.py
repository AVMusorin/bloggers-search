from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def search(request):
    return render(request, 'frontend/search_form.html')
