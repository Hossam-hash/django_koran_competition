from django.urls import path
from . import views


urlpatterns=[
path('apply_compition',views.apply_compition,name='apply_compition'),
path('enter_results',views.enter_results,name='enter_results'),
path('show_results',views.show_results,name='show_results'),
path('search',views.search,name='search'),


]