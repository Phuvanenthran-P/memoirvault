from django.urls import path
from . import views

urlpatterns = [
    path("", views.moment_list, name="moment_list"),
    path("create/", views.moment_create, name="moment_create"),
    path("<int:pk>/edit/", views.moment_update, name="moment_update"),
    path("<int:pk>/delete/", views.moment_delete, name="moment_delete"),
]

