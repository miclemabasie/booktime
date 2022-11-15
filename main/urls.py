from django.urls import path
from .views import home_page as home
from .views import about_us_page

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about_us_page, name="about"),
]
