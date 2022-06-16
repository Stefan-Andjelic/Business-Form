from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def main(request):
    return render(request, 'main/home.html')


def post_share(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            subject = f"New quote from {cd['name']}"
            message = f"{cd['name']} has a quote for you! {cd['email']} \n\n Here are his comments: \n {cd['comments']}"
            send_mail(subject, message, 'stefanandjelic8@gmail.com', [cd['to']])
            sent = True
    else:
        form = ContactForm()
    return render(request, 'main/share.html', {'form': form, 'sent': sent})
