from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<str:username>/', views.user_detail, name='user_detail'),
]