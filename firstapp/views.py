from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
#from django.urls import render
def index(request):
    return HttpResponse("Hello word.Hello dept CSE")
def dataRender2(request):
    return HttpResponse("Hello Mbstu")
def htmlPage(request):
    return render(request,'index.html')

def htmlPage1(request):
    return render(request,'home2.html')


def new():
    return None