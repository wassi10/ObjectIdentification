from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Result(request):
    return render(request, 'result.html')