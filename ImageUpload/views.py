from django.shortcuts import render

def handle_uploaded_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def Home(request):
    return render(request, 'index.html')

def Result(request):
    return render(request, 'result.html')