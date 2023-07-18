from django.urls import path
from .views import (
    index,
    ForemanCreateView,
    ForemanListView,
    ForemanDetailView,
    ForemanUpdateView,
    ForemanDeleteView,
    WorkCommitmentsListView,
    WorkCommitmentsCreateView,
    WorkCommitmentsUpdateView,
    WorkCommitmentsDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "foreman/create/",
        ForemanCreateView.as_view(),
        name="foreman-create"
    ),
    path("foreman/", ForemanListView.as_view(), name="foreman-list"),
    path(
        "foreman/<int:pk>/",
        ForemanDetailView.as_view(),
        name="foreman-detail"
    ),
    path(
        "foreman/<int:pk>/update/",
        ForemanUpdateView.as_view(),
        name="foreman-update",
    ),
    path(
        "foreman/<int:pk>/delete/",
        ForemanDeleteView.as_view(),
        name="foreman-delete",
    ),
    path(
        "work-commitments/",
        WorkCommitmentsListView.as_view(),
        name="work-commitments-list"
    ),
    path(
        "work-commitments/create",
        WorkCommitmentsCreateView.as_view(),
        name="work-commitments-create"
    ),
    path(
        "work-commitments/<int:pk>/update",
        WorkCommitmentsUpdateView.as_view(),
        name="work-commitments-update"
    ),
    path(
        "work-commitments/<int:pk>/delete",
        WorkCommitmentsDeleteView.as_view(),
        name="work-commitments-delete"
    ),
]

app_name = "hall"
