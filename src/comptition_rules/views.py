from django.shortcuts import render
from .models import Comptition_Rules
# Create your views here.
def comptition_rules(request):
    context={

        'ruless':Comptition_Rules.objects.all()
    }
    return render(request,'comptition_rules/comptition_rules.html',context)