import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import SpeedViolation
from django.contrib import messages
from django.core.paginator import Paginator



# Create your views here.

#Homepage View
class HomePage_View(View):
    def get(self, request):
        return render(request, 'Partials/others.html')


#Search form View
def search_form(request):
    return render(request, 'Search/search_form.html')

def search_form_all(request):
    return render(request, 'Search/search_form_all.html')

#Search penalties View


def search_result(request):
    context = dict()
    context['searched'] = False
    if request.method == 'POST':
        context['searched']=True
        search_content = request.POST.get('number_plate')
        try:
            speed_violation = SpeedViolation.objects.all().filter(number_plate__icontains=search_content, status = 'Unpaid').order_by('-number_plate').values('number_plate', 'speed_limit', 'car_speed', 'location', 'fine_amount', 'status')
            context['speed_violation'] = speed_violation
            print(context)
        except Exception:
            pass
    return render(request, 'Search/search_results.html', context)


def search_result_all(request):
    context = dict()
    context['searched'] = False
    if request.method == 'POST':
        context['searched']=True
        search_content = request.POST.get('number_plate')
        try:
            speed_violation_all = SpeedViolation.objects.all().filter(number_plate__icontains=search_content).order_by('-number_plate').values('number_plate', 'speed_limit', 'car_speed', 'location', 'status', 'fine_amount')
            context['speed_violation_all'] = speed_violation_all
            print(context)
        except Exception:
            pass
    return render(request, 'Search/search_results_all.html', context)



def record_all(request):
    violations = SpeedViolation.objects.all()
    paginator = Paginator(violations, 3)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'violations': violations,
        'page_obj': page_obj,
    }
    return render(request, 'Search/table.html', context)

def filter_record(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('search')
        violationsearch = SpeedViolation.objects.filter(status__istartswith= search_str) | SpeedViolation.objects.filter(location__istartswith= search_str) | SpeedViolation.objects.filter(record_date__istartswith= search_str) | SpeedViolation.objects.filter(number_plate__istartswith = search_str) 
        data = violationsearch.values()
        return JsonResponse(list(data), safe=False)
    