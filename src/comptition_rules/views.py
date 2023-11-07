from django.shortcuts import render

# Create your views here.
def comptition_rules(request):
    return render(request,'comptition_rules/comptition_rules.html')