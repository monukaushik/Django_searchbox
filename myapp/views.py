from django.shortcuts import render
from .models import *
from django.db.models import Q
import contextlib

# Create your views here.
def index(request):
   data=Student.objects.all()
   if request.method =='GET':
      text_search=request.GET.get('input_text')
      with contextlib.suppress(Exception):
            # use for multipal fields search
            loopupvalue=Q(username__icontains=text_search)|Q(city__icontains=text_search)|Q(state__icontains=text_search)|Q(status__icontains=text_search)
            
            # use for single field search
            # data2=Student.objects.filter(username__icontains=text_search)
            data2=Student.objects.filter(loopupvalue)
            return render(request,'index.html',{'data':data2})
   return render(request,'index.html',{'data':data})  