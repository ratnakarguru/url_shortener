from django.urls import path
from .views import home, redirect_url, login_view, signup

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/',signup,name='signup'),
    path('<str:short_code>/', redirect_url, name='redirect-url'),
    
]
