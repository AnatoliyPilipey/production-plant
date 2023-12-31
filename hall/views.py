from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Shift, Foreman, WorkCommitments, Workman
from .forms import (
    ForemanCreationForm,
    SearchForm,
    ShiftForm,
)


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


class ForemanUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Foreman
    fields = ["username", "first_name", "last_name", "salary"]
    success_url = reverse_lazy("hall:foreman-list")


class ForemanDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Foreman
    success_url = reverse_lazy("hall:foreman-list")


class WorkCommitmentsListView(LoginRequiredMixin, generic.ListView):
    model = WorkCommitments
    template_name = "hall/work_commitments_list.html"
    context_object_name = "work_commitments_list"
    paginate_by = 3


class WorkCommitmentsCreateView(LoginRequiredMixin, generic.CreateView):
    model = WorkCommitments
    fields = "__all__"
    template_name = "hall/work_commitments_form.html"
    success_url = reverse_lazy("hall:work-commitments-list")


class WorkCommitmentsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = WorkCommitments
    fields = "__all__"
    template_name = "hall/work_commitments_form.html"
    success_url = reverse_lazy("hall:work-commitments-list")


class WorkCommitmentsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = WorkCommitments
    template_name = "hall/work_commitments_confirm_delete.html"
    success_url = reverse_lazy("hall:work-commitments-list")


class WorkmanListView(LoginRequiredMixin, generic.ListView):
    model = Workman
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkmanListView, self).get_context_data(**kwargs)

        username_ = self.request.GET.get("value_", "")

        context["search_form"] = SearchForm(
            initial={"value_": username_}
        )
        return context

    def get_queryset(self):
        queryset = Workman.objects.select_related("commitment")
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                first_name__icontains=form.cleaned_data["value_"]
            )
        return queryset


class WorkmanDetailView(LoginRequiredMixin, generic.DetailView):
    model = Workman
    queryset = Workman.objects.select_related("commitment")
#    queryset = Workman.objects.prefetch_related("workman_to_day__foreman")


class WorkmanCreateView(LoginRequiredMixin, generic.CreateView):
    model = Workman
    fields = "__all__"
    success_url = reverse_lazy("hall:workman-list")


class WorkmanUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Workman
    fields = "__all__"
    success_url = reverse_lazy("hall:workman-list")


class WorkmanDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Workman
    success_url = reverse_lazy("hall:workman-list")


class ShiftListView(LoginRequiredMixin, generic.ListView):
    model = Workman
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShiftListView, self).get_context_data(**kwargs)

        username_ = self.request.GET.get("value_", "")

        context["search_form"] = SearchForm(
            initial={"value_": username_}
        )
        return context

    def get_queryset(self):
        queryset = Shift.objects.select_related("foreman")
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                work_date__icontains=form.cleaned_data["value_"]
            )
        return queryset


class ShiftDetailView(LoginRequiredMixin, generic.DetailView):
    model = Shift

    def get_queryset(self):
        return Shift.objects.prefetch_related("workman")


class ShiftCreateView(LoginRequiredMixin, generic.CreateView):
    model = Shift
    form_class = ShiftForm
    success_url = reverse_lazy("hall:shift-list")


class ShiftUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Shift
    form_class = ShiftForm
    success_url = reverse_lazy("hall:shift-list")


class ShiftDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Shift
    success_url = reverse_lazy("hall:shift-list")
