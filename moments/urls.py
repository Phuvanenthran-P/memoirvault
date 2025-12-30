from django.urls import path
from .views import moment_list

urlpatterns = [
    path("", moment_list, name="moment_list"),
]
