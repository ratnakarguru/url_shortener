from django.urls import path
from .views import home, redirect_url , dashboard, generate_qr

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/',dashboard,name='dashboard'),
    path('<str:short_code>/', redirect_url, name='redirect-url'),
    path('qr/<str:short_code>/', generate_qr, name='generate_qr'),
]