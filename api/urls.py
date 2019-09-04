from django.urls import path
from api import views

urlpatterns = [
    path('api/bloggers/<int:pk>/', views.blogger_detail),
    path('api/bloggers', views.get_bloggers)
]
