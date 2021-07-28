from django.shortcuts import get_object_or_404, render
from .models import Introduce

# Create your views here.

def home(request):
    return render(request, "home.html")
    
def hobby(request):
    return render(request, "hobby.html")

def music(request):
    return render(request, "music.html")

def picture(request):
    return render(request, "picture.html")

def place(request):
    return render(request, "place.html")

def rollingpaper(request):
    rollingpaper_body = Introduce.objects.all()
    return render(request, "rollingpaper.html", {'rollingpaper_body':rollingpaper_body})

def detail(request, id):
    rollingpaper_contents = get_object_or_404(Introduce, pk = id)
    return render(request, "detail.html", {'rollingpaper_contents':rollingpaper_contents})