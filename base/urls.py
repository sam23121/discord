from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<str:pk>/', views.index, name='index'),
]