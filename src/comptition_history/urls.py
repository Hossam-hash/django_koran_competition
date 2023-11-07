from django.urls import path
from . import views


urlpatterns=[

path('comptition_history',views.comptition_history,name='comptition_history'),]