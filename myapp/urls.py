from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',view=Index,name='Index'),
    path('formdata',formdata,name='formdata')
]