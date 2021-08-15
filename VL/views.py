from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return render(request, 'index.html')


def value(request):
    main_text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    
    if removepunc=='on':
        punctuations=''' ;.:'.'_-/,'][;] '''
        analyzed=''
        for char in main_text:
            if char not in punctuations:
                analyzed=analyzed + char

        params = {'purpose':'Removed punctuaion','analyzed_text':analyzed}         
        return render(request, '2.html', params)

    elif fullcaps=='on':
        analyzed=''
        for char in main_text:
            analyzed= analyzed + char.upper()


        params = {'purpose':'Changed to upper case','analyzed_text':analyzed}         
        return render(request, '2.html', params)

    elif newlineremover=='on':
        analyzed=''
        for char in main_text:
            if char != "\n" and char != '\r':
                analyzed=analyzed + char

        params = {'purpose':'Removed punctuaion','analyzed_text':analyzed}         
        return render(request, '2.html', params)





    else:
        return HttpResponse('ERROR <br> please select any option')


# Create your views here.

    