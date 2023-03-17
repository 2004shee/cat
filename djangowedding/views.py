from django.shortcuts import render


def STORY(request):
    return render(request,'about.html')
def HOME(request):
    return render(request , 'index.html')
def GALLERY(request):
    return render(request ,'gallery.html')
def SERVICES(request):
    return render(request,'services.html')
def CONTACT (request):
    return render(request, 'contact.html')
