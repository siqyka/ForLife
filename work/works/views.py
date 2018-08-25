# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from .models import *
from django.core import serializers
# Create your views here.


def work_views(request):
    houses=Houses.objects.all().values_list('radd','rurl') 
    jobs=Jobs.objects.all().values_list('sadd','joburl','position')

    job=[]
    house=[]
    for i in houses:
        house.append(list(i))

    for x in jobs:
        job.append(list(x))   

    dic={
    'job':json.dumps(job),
    'house':json.dumps(house)
    }

    print(Houses)
    return render(request,'work.html',dic)

