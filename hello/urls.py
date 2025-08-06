from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rafa", views.rafa, name="rafa"),
    path("<str:name>", views.greeting, name="greeting")
]