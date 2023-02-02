from django.shortcuts import render
from pytube import *
from pathlib import Path
import os
from wsgiref.util import FileWrapper
from django.utils import timezone


# Create your views here.
def index(request):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
    msg = ''

    if request.method == 'POST':
        link = request.POST['link'] 
        quality = request.POST['quality']
        file = BASE_DIR/'downloads/'

        if quality == '1080p' and link != '':
            video = YouTube(link) 
            try:
                yt = video.streams.filter(res = '1080p', file_extension = 'mp4').first()
                yt.download(file)
                msg = 'Video downloaded in LQ'
                path = str(file)
                return render(request,'ythome/index.html',{'status': msg +' in '+ path})
            except:
                 msg = 'Quality not Available'
                 return render(request,'ythome/index.html',{'status': msg })


                
        elif quality == '720p' and link != '':
            video = YouTube(link)
            try:
                yt = video.streams.filter(res = '720p', file_extension = 'mp4').first()
                yt.download(file)
                msg = 'Video Downloaded'
                path = str(file)
                return render(request,'ythome/index.html',{'status': msg +' in '+ path})
            except:
                 msg = 'Quality not Available'
                 return render(request,'ythome/index.html',{'status': msg })

        elif quality == '480p' and link != '':
            video = YouTube(link) 
            try:
                yt = video.streams.filter(res = '480p', file_extension = 'mp4').first()
                yt.download(file)
                msg = 'Video Succesfully downloaded'
                path = str(file)
                return render(request,'ythome/index.html',{'status': msg +' in '+ path})
            except:
                 msg = 'Format not Available'
                 return render(request,'ythome/index.html',{'status': msg })

        elif quality == '360p' and link != '':
            video = YouTube(link) 
            try:
                yt = video.streams.filter(res = '360p', file_extension = 'mp4').first()
                yt.download(file)
                msg = 'Video Succesfully downloaded'
                path = str(file)
                return render(request,'ythome/index.html',{'status': msg +' in '+ path})
            except:
                 msg = 'Format not Available'
                 return render(request,'ythome/index.html',{'status': msg })

        elif quality == 'mp3' and link != '':
            video = YouTube(link) 
            try:
                yt = video.streams.filter(only_audio=True,  abr="128kbps").first()
                yt.download(file)
                msg = 'Audio Succesfully downloaded'
                path = str(file)
                return render(request,'ythome/index.html',{'status': msg +' in '+ path})
            except:
                 msg = 'Format not Available'
                 return render(request,'ythome/index.html',{'status': msg })                 
        else:
            msg = 'error encountered'
            return render(request,'ythome/index.html',{'status':msg +' in '+ msg})    



    return render(request,'ythome/index.html')  

def index2(request) :
    return render(request,'ythome/index2.html')