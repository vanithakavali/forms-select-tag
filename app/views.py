from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        nm=request.POST['nm']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=ur)[0]
        WO.save()
        return HttpResponse('webpage data is inserted')
    return render(request,'insert_webpage.html',d)

def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MSTS=request.POST.getlist('tn')
        print(MSTS)
        WOS=Webpage.objects.none()
        for i in MSTS:
            WOS=WOS|Webpage.objects.filter(topic_name=i)
        d1={'WOS':WOS}
        return render(request,'display_webpage.html',d1)

    return render(request,'retrive_webpage.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)



