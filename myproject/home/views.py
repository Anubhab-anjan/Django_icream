from django.shortcuts import render , HttpResponse


def index(request):
    context = {
        "variable": "This is sent"
    }
    # return HttpResponse("Hello, this is the home page!")
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("Hello, this is the services page!")

def contact(request):
    return render(request,'contact.html')