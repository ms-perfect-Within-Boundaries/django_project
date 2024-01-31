from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#create views
def print_hello(request):
    return render(request,'hello.html')




from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):
    template_name = 'home/login.html'  # Create this template