from django.urls import path
from . import views

urlpatterns = [
    path("", views.moment_list, name="moment_list"),
    path("create/", views.moment_create, name="moment_create"),
]
