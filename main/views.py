from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.urls import reverse


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
        "description": "Booktime is a company that sells books online.",
        "header": "ABOUT BOOKTIME",
        "form": contact_form,
    }
    template_name = "main/about.html"

    return render(request, template_name, context)


def contact_us(request):
    contact_us_form = ContactForm(request.POST or None)
    template_name = "main/contact_form.html"

    if contact_us_form.is_valid():
        contact_us_form.send_mail()
        return redirect(reverse("main:home"))
    context = {
        "form": contact_us_form,
    }

    return render(request, template_name, context)


# Class version
class ContactUsView(FormView):
    template_name = "main/contact_form.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
