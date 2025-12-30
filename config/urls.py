from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Dashboard placeholder")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", dashboard, name="dashboard"),

]
