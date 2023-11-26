from django.shortcuts import render
from .models import Comptition_History
# Create your views here.
def comptition_history(request):
    history=Comptition_History.objects.all()
    context = {
        'history': history
    }
    return render(request,'comptition_history/comptition_history.html',context)