from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Shift, Foreman
from .forms import ForemanCreationForm, SearchForm


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


class ForemanListView(LoginRequiredMixin, generic.ListView):
    model = Foreman
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ForemanListView, self).get_context_data(**kwargs)

        username_ = self.request.GET.get("value_", "")

        context["search_form"] = SearchForm(
            initial={"value_": username_}
        )
        return context

    def get_queryset(self):
        queryset = Foreman.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["value_"]
            )
        return queryset


class ForemanDetailView(LoginRequiredMixin, generic.DetailView):
    model = Foreman
