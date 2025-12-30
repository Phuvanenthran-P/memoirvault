from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Moment

@login_required
def moment_list(request):
    moments = Moment.objects.filter(owner=request.user)
    return render(request, "moments/moment_list.html", {"moments": moments})
