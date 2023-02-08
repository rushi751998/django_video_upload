from django.shortcuts import render,HttpResponse,redirect
from .forms import Video_form
from .models import Video,person_db
from math import ceil

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


def images(request):
    face_id = person_db.objects.all()
    # gender = person_db.objects.all()
    # age = person_db.objects.all()
    # emotions = person_db.objects.all()
    # race = person_db.objects.all()
    # images = person_db.objects.all()
    n = len(face_id)
    nslides = n//4+ceil((n/4)-(n//4))
    
    db_points = [[]]
    param = {'db_points':face_id,'no_slides':nslides,'range':range(0,n)}
    return render(request,'images.html',param)

