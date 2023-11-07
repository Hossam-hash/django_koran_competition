from django.urls import path
from . import views


urlpatterns=[

path('comptition_rules',views.comptition_rules,name='comptition_rules'),]