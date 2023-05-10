from django.urls import path

from recipes.views import about, contact, home

# HTTP REQUEST
urlpatterns = [
    path("", home),  # Home
    path("about/", about),  # /sobre/
    path("contact/", contact),  # /contato
]
