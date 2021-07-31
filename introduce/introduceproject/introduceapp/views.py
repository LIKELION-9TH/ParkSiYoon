from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Introduce

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def hobby(request):
    return render(request, 'hobby.html')

def music(request):
    return render(request, 'music.html')

def picture(request):
    return render(request, 'picture.html')

def place(request):
    return render(request, 'place.html')

def rollingpaper(request):
    rollingpaper_body = Introduce.objects.all()
    return render(request, 'rollingpaper.html', {'rollingpaper_body':rollingpaper_body})

def detail(request, id):
    rollingpaper_contents = get_object_or_404(Introduce, pk = id)
    return render(request, 'detail.html', {'rollingpaper_contents':rollingpaper_contents})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_introduce = Introduce()
    new_introduce.title = request.POST['title']
    new_introduce.writer = request.POST['writer']
    new_introduce.body = request.POST['body']
    new_introduce.date = timezone.now()
    new_introduce.save()
    return redirect('detail',new_introduce.id)

def edit(request, id):
    edit_introduce = Introduce.objects.get(id= id)
    return render(request, 'edit.html', {'rollingpaper_contents':edit_introduce})

def update(request, id):
    update_introduce = Introduce.objects.get(id= id)
    update_introduce.title = request.POST['title']
    update_introduce.writer = request.POST['writer']
    update_introduce.body = request.POST['body']
    update_introduce.date = timezone.now()
    update_introduce.save()
    return redirect('detail', update_introduce.id)

def delete(request, id):
    delete_introduce = Introduce.objects.get(id = id)
    delete_introduce.delete()
    return redirect('rollingpaper')


