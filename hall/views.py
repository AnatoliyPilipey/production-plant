from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Shift, Foreman
from .forms import ForemanCreationForm


def index(request):
    """View function for the home page of the site."""

    num_shifts = Shift.objects.count()
    num_foreman = Foreman.objects.count()
    sum_products = Shift.objects.all().aggregate(production=Sum("products_produced"))
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_shifts": num_shifts,
        "num_foreman": num_foreman,
        "sum_products": sum_products["production"],
        "num_visits": num_visits + 1,
    }

    return render(request, "hall/index.html", context=context)


class ForemanCreateView(LoginRequiredMixin, generic.CreateView):
    model = Foreman
    form_class = ForemanCreationForm
    success_url = reverse_lazy("hall:index")
