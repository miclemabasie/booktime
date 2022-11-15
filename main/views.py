from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def home_page(request):

    context = {}

    template_name = "main/home.html"
    return render(request, template_name, context)


def about_us_page(request):
    contact_form = ContactForm(request.POST or None)

    send_mail(
        "Test subject",
        "message",
        "miclemabasie@mail.com",
        [
            "booktim@site.com",
        ],
    )

    context = {
        "description": "This is all about the services we offer at booktime.",
        "header": "ABOUT BOOKTIME",
        "form": contact_form,
    }
    template_name = "main/about.html"

    return render(request, template_name, context)
