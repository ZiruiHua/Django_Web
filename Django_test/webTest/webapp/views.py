#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import pyodbc
import pandas as pd
# Create your views here.
def home(request):
    return render(request, 'home.html')

def ajax_list(request):
    a = range(100)
    index_dict = {'index_insert':a}
    return render(request, '.html', context = index_dict)

def index(request):
    return render(request, 'valuepass.html')

def valuePass(request):
    para1 = request.GET['a']
    para2 = request.GET['b']
    #insert query here
    # conn = pyodbc.connect(r'Driver={SQL Server};Server=ZIRUIH;Database=BDCI_AutoHome;Trusted_Connection=yes;')
    # sql = "SELECT number,province_pinyin FROM DM_AutoHome_Map"
    # df = df = pd.read_sql_query(sql, conn)
    # list = [para1,para2]
    # df = df[df['province_pinyin'].isin(list)]
    # result = df['number'].tolist()[0]
    # result = [para1,para2]
    # dict = {'valueFromView':result}
    # return render(request, 'valueresult.html', context = dict)
    return HttpResponse(para2)
