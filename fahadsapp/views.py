from http.client import RemoteDisconnected
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    topclient=client.objects.all()
    b =[]
    for i in topclient:
        b.append(i)
    clientthumb=b[::-1]
    uploadPortfolio=UploadPortfolio.objects.all()
    a =[]
    for i in uploadPortfolio:
        a.append(i)
    uploadthumb=a[::-1]
    catagory=Category.objects.all()
    return render(request,'index.html',{'catagory':catagory,'uploadPortfolio':uploadthumb,'client':clientthumb})



def show(request):
    uploadPortfolio=UploadPortfolio.objects.all()
    a =[]
    for i in uploadPortfolio:
        a.append(i)
    uploadthumb=a[::-1]
    catagory=Category.objects.all()
    return render(request,'show.html',{'catagory':catagory,'uploadPortfolio':uploadthumb})


def prod(request,id):
    uploadPortfolio=UploadPortfolio.objects.filter(id=id)
    return render(request,'prod.html',{'uploadPortfolio':uploadPortfolio})