from django.urls import path, include
from . import views
from .views import Login_View
urlpatterns = [
    path('', views.home, name="Home"),
    path('camera_image/', views.camera_images, name='camera_image'),
    path('login', Login_View.as_view(), name='login'),
    path('Dashboard', views.dashboard, name='Dashboard'),
]
