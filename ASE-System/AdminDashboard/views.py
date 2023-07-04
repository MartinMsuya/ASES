from django.shortcuts import render
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def admin_dashboard(request):
    return render(request, 'AdminDashboard/dashboard.html', {'user': request.user})


def chart_visualization(request):
    return render(request, "AdminDashboard/streamlit.html")