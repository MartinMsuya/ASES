import json
from urllib import response
import requests
from pprint import pprint
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from .models import Numberplate, Test
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.
# Create your views here.


@csrf_exempt
def camera_images(request):
    # try:
    file =  request.FILES['file']
    default_storage.save(file.name, file)
    regions = ['Dar', 'tz'] # Change to your country
    with open(os.path.join(settings.MEDIA_ROOT, file.name), 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions),  # Optional
            files=dict(upload=fp),
            headers={'Authorization': 'Token 97b701930466ea9f17b39d28a213ea9b8ff8fffe'})
        
    #pprint(response.json())
    data = response.json()
    no_plate =(data['results'][0]['plate'])
    no_plate=str(no_plate).upper()
    # Save the number plate to the database
    number_plate_obj = Test(Image=file.name, plate=no_plate)
    number_plate_obj.save()

    return HttpResponse(json.dumps({"status": "1", "message": "Sucess"}), content_type = 'application/json')
    # except Exception as e:
    #     return HttpResponse(json.dumps({"status": "0", "message": "Fail", "error": str(e)}), content_type = 'application/json')


def home (request):
    return render(request, "Home.html")

def dashboard(request):
    return render(request, 'base.html')

class Login_View(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username=request.POST.get('usernamelog')
        password = request.POST.get('password')
        if username and password:
            user=auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('Dashboard')
                else:
                    messages.error(request, 'Account requested is not activate please contant your admin')
                return render(request, 'login.html')
            messages.error(request, 'Invalid credential, please provide correct info')
            return render(request, 'login.html')
        messages.error(request, 'Please fill all fields')
        return render(request, 'login.html')

