from django.shortcuts import render

# Create your views here.

def hahaha(request):
    if request.method == "GET":
        return render(request,'hahaha.html')
    else:
        return



