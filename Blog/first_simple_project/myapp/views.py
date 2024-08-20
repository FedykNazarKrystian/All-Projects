from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    data = {
        "title": "MAIN PAGE",
        "values": ['Red', 'Blue', 'Green'],
        "objects": {
            "car": "Mercedes",
            "model": "Van",
            "year": 2020
        }
    }
    return render(request, 'myapp/index.html', data)

def about(request):
    #return HttpResponse("<h4>About</h4>")
    return render(request, 'myapp/about.html')

def contact(request):
    #return HttpResponse("<h4>About</h4>")
    return render(request, 'myapp/contact.html')

