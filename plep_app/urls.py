from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('register/', views.register, name='register'),
    path('verification/', views.uid, name='uid'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard')
]
