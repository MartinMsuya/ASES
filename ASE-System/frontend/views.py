import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from Backend.models import Numberplate
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
            speed_violation = Numberplate.objects.all().filter(No_plate__icontains=search_content, Status = 'Unpaid').order_by('-Record_date').values('No_plate', 'Car_speed', 'Location', 'Fine_amount', 'Status', 'Record_date')
            context['speed_violation'] = speed_violation
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
            speed_violation_all = Numberplate.objects.all().filter(No_plate__icontains=search_content).order_by('-Record_date').values('No_plate', 'Car_speed', 'Location', 'Fine_amount', 'Status', 'Record_date')
            context['speed_violation_all'] = speed_violation_all
        except Exception:
            pass
    return render(request, 'Search/search_results_all.html', context)



def record_all(request):
    violations = Numberplate.objects.all()
    paginator = Paginator(violations, 10)
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
        violationsearch = Numberplate.objects.filter(Status__istartswith= search_str) | Numberplate.objects.filter(Location__istartswith= search_str) | Numberplate.objects.filter(Record_date__istartswith= search_str) | Numberplate.objects.filter(No_plate__istartswith = search_str) 
        data = violationsearch.values()
        return JsonResponse(list(data), safe=False)
    