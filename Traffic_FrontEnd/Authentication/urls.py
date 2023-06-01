from django.urls import path
from .views import Login_View
from django.views.decorators.cache import never_cache
from . import views
app_name= 'authentication'
urlpatterns = [
    path('login', never_cache(Login_View.as_view()), name='login'), 
    path('logout', views.logoutUSer, name='logout'), 
    path('register', views.registeruser, name='register'), 
]
