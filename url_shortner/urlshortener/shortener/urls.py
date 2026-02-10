from django.urls import path
from .views import home, redirect_url , dashboard

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/',dashboard,name='dashboard'),
    path('<str:short_code>/', redirect_url, name='redirect-url'),
]