from django.shortcuts import render
from comptition_history.models import Comptition_History
from comptition_rules.models import Comptition_Rules
# Create your views here.
def home(request):

    context = {
        'history': Comptition_History.objects.all(),
        'ruless': Comptition_Rules.objects.all()
    }
    return render(request,'home/home.html',context)