from django.shortcuts import render,HttpResponse,redirect
from .forms import Video_form
from .models import Video

def index(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form=Video_form()
        return render(request,'index.html',{"form":form})
    
def videos(request):
    all_video=Video.objects.all()
    return render(request,'videos.html',{"all":all_video})

