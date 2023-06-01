from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
import datetime
import json
from Custome.models import SpeedViolation

# Create your views here.
@login_required
def admin_dashboard(request):
    return render(request, 'AdminDashboard/dashboard.html', {'user': request.user})


def chart_visualization(request):
    today_date = datetime.date.today()
    record = SpeedViolation.objects.filter(date__lte=today_date)
    finalrep = { }

    def get_location():
        return SpeedViolation.location
    location_list =list(set(map(get_location, record)))
    
    def get_location_fine_amount(location):
        fine_amount = 0
        filtered_by_location = record.filter(location = location)
        for item in filtered_by_location:
            fine_amount += item.fine_amount
        return fine_amount
    
    for x in record:
        for y in location_list:
            finalrep[y]=get_location_fine_amount(y)
    return JsonResponse({'get_location_fine_amount': finalrep}, safe=False)



def statsView(request):
    return render(request, 'AdminDashboard/statis.html')