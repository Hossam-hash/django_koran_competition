from django.shortcuts import render

# Create your views here.
def apply_compition(request):
    return render(request,'students/apply_comptition.html')
def enter_results(request):
    return render(request,'students/enter_results.html')
def search(request):
    return render(request,'students/search.html')
def show_results(request):
    return render(request,'students/show_results.html')