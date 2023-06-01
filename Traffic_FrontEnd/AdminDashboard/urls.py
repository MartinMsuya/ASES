from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
app_name= 'admindashboard'

urlpatterns = [
    path('admin1/', views.admin_dashboard, name='admin1'), 
    path('chart/', views.chart_visualization, name='chart'), 
    path('statschat/', views.statsView, name='statschart'), 
]

