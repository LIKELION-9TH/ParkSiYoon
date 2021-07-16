from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def free(request):
    return render(request, "free.html")

def hobby(request):
    return render(request, "hobby.html")

def music(request):
    return render(request, "music.html")

def pictures(request):
    return render(request, "pictures.html")

def place(requests):
    return render(request, "place.html")

