from django.shortcuts import render
from . forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['nurfachridaffa17@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('success/')
    else:
        form = ContactForm()
    
    context = {
        'form' : form
    }
    return render(request, 'Contact/contact.html', context)

def send_success(request):
    return render(request, 'Contact/success.html')