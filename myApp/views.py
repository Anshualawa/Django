from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('<h1> This is HttpResponce!</h1>')
    return render(request,'index.html')
