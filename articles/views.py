from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'articles/index.html')

def about(request):
    return render(request, 'articles/about.html');