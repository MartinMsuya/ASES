from django.urls import path
from .views import HomePage_View
from . import views
from django.views.decorators.csrf import csrf_exempt
app_name = 'custome'
urlpatterns = [
    path('', HomePage_View.as_view(), name="Homepage"),
    path('search_form/', views.search_form, name='search_form'),
    path('search_form_all/', views.search_form_all, name='search_form_all'),
    path('search_result/', views.search_result, name='search_result'),
    path('search_result_all/', views.search_result_all, name='search_result_all'),
    path('Record_all/', views.record_all, name="all_record"),
    path('search', csrf_exempt(views.filter_record), name='search'),
]
