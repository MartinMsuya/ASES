from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache




# Create your views here.
def registeruser(request):
    return render(request, 'Partials/register.html')

class Login_View(View):
    def get(self, request):
        return render(request, 'Authentication/login.html')
    def post(self, request):
        username=request.POST.get('usernamelog')
        password = request.POST.get('password')
        if username and password:
            user=auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome '+ 
                                     user.username + ' you are now logged in')
                    return redirect('custome:Homepage')
                else:
                    messages.error(request, 'Account requested is not activate please contant your admin')
                return render(request, 'Authentication/login.html')
            messages.error(request, 'Invalid credential, please provide correct info')
            return render(request, 'Authentication/login.html')
        messages.error(request, 'Please fill all fields')
        return render(request, 'Authentication/login.html')
 

@never_cache
def logoutUSer(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('authentication:login')

# Create your views here.
