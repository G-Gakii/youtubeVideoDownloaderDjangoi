from django.shortcuts import render,redirect
from pytube import YouTube
from django.contrib import messages
from pytube.exceptions import VideoUnavailable

# Create your views here.
def youtubeDownload(request):
    if request.method=="POST":
        link=request.POST.get("link")
        if not link:
            messages.error(request,"No url provided")
            return render(request,'url.html')
        try:
            video=YouTube(link)
            stream=video.streams.get_highest_resolution()
            stream.download()
            messages.success(request,"video successfully downloaded")
        except VideoUnavailable:
            messages.error(request,"The video unavailable")
        except Exception as e:
            messages.error(request,"f'an error occurred : {e}")

        return render(request,'url.html')
    return render(request,'url.html')


