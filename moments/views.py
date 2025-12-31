from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Moment
from .forms import MomentForm


@login_required
def moment_list(request):
    moments = Moment.objects.filter(owner=request.user)
    return render(request, "moments/moment_list.html", {"moments": moments})


@login_required
def moment_create(request):
    if request.method == "POST":
        form = MomentForm(request.POST, request.FILES)
        if form.is_valid():
            moment = form.save(commit=False)
            moment.owner = request.user
            moment.save()
            return redirect("moment_list")
    else:
        form = MomentForm()

    return render(request, "moments/moment_form.html", {"form": form})


@login_required
def moment_update(request, pk):
    moment = get_object_or_404(Moment, pk=pk, owner=request.user)

    if request.method == "POST":
        form = MomentForm(request.POST, request.FILES, instance=moment)
        if form.is_valid():
            form.save()
            return redirect("moment_list")
    else:
        form = MomentForm(instance=moment)

    return render(request, "moments/moment_form.html", {"form": form})


@login_required
def moment_delete(request, pk):
    moment = get_object_or_404(Moment, pk=pk, owner=request.user)

    if request.method == "POST":
        moment.delete()
        return redirect("moment_list")

    return render(request, "moments/moment_confirm_delete.html", {"moment": moment})
