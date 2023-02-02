from django.urls import path
from . import views

app_name = 'ytadmin'

urlpatterns = [
 path('',views.index,name='index'),
 path('index2',views.index2,name='index2')
]           