from django.shortcuts import render

def htmlpage(request):
    return render(request,'theme/index.html')