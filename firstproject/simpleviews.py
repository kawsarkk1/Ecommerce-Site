from django.shortcuts import render

def htmlPage(request):
    return render(request,'theme/index.html')