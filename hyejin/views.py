from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ImageForm 
from .models import Upload



# Create your views here.
def main(request):
    return render(request,'main.html')

# def index(request):
#     global img
#     if request.method == "POST":
#         form=ImageForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # return render(request,"index.html",)
#     else:
#         form=ImageForm()
#         img = Upload.objects.all()
#     return render(request,"index.html",{"img":img,"form":form})


def index(request):
    global img
    if request.method == "POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    form=ImageForm()
    img = Upload.objects.all()
    return render(request,"index.html",{"img":img,"form":form})



 
