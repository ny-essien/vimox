from django.shortcuts import render, redirect
from .forms import Profile, ContactForm
from django.contrib import messages

# Create your views here.
def profile(request):

    page = 'profile'

    if request.method == "POST":

        form = Profile(request.POST)

        if form.is_valid():
            messages.success(request, 'Saved')
            return redirect('profile')

    else:

        context = {

            'forms':Profile(),
            'page':page,
        }
        return render(request, 'forms.html', context)


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']

            if cc_myself:
                recipients.append(sender)
                from django.core.mail import send_mail
                send_mail(subject, message, sender, recipients)
                return redirect('profile')

    return render(request, 'forms.html', {'forms':ContactForm(), 'page':'contact'})