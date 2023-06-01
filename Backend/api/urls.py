from django.urls import path, include
from . import views
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('getroutes/', views.getRioutes),
    path('project/<str:pk>/', views.getProject),
    path('projects/', views.getProjects),
    path('', include(router.urls)),
]