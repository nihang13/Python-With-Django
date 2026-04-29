from django.shortcuts import render
from .models import Course

# Create your views here.
def home(request):
    data=Course.objects.all() #query set
    return render(request,"home.html",{'data':data})