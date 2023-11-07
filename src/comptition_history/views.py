from django.shortcuts import render

# Create your views here.
def comptition_history(request):
    return render(request,'comptition_history/comptition_history.html')