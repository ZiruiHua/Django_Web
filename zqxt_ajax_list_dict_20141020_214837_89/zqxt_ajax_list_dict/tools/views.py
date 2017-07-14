from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'index.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def add1(request):
    a = request.GET['a']
    result = json.loads(a)

    # sum1 = 0
    # for x in a:
    #     sum1+=int(x)

    return HttpResponse(result[0])

import json

def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    list1 = [
    ['Year', 'Sales', 'Expenses'],
    ['2004',  1000,      400],
    ['2005',  1170,      460],
    ['2006',  660,       1120],
    ['2007',  1030,      540]
    ]
    name_dict = {'twz': list1}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')
