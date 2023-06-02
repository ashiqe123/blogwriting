from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def view(request):
    return render(request,"viewpage.html")

def post2(request):
    return render(request,'post2.html')

def post3(request):
    return render(request,'post3.html')
