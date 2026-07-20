from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    return HttpResponse("<h1>Contact Us Page</h1><p>this is a page</p>")

def about_view(request):
    return HttpResponse("<h1>About Us Page</h1><p>this is a page</p>")
