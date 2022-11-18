from django.urls import path
from .views import home_page as home
from .views import about_us_page, contact_us, ContactUsView

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about_us_page, name="about"),
    path("contact/", contact_us, name="contact_us"),
    # class version for contact us page
    path("class_contact/", ContactUsView.as_view(), name="class_contact"),
]
