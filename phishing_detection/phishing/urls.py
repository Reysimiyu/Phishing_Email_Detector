from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('analyze', views.analyze_email, name='analyze_email'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
