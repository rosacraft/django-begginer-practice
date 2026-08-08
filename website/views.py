from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect

def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            # back to the main page
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def about_view(request):
    return render(request, 'website/about.html')

def test_view(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
            
    form = ContactForm()
    
    return render(request, 'test.html', {'form': form})
