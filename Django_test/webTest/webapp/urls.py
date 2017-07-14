from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^pass/', views.index, name='valuepass'),
    url(r'^showresult/', views.valuePass, name='result'),
]
