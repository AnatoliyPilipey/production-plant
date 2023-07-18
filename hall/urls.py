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
    WorkmanListView,
    WorkmanDetailView,
    WorkmanCreateView,
    WorkmanUpdateView,
    WorkmanDeleteView,
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
        "work-commitments/create/",
        WorkCommitmentsCreateView.as_view(),
        name="work-commitments-create"
    ),
    path(
        "work-commitments/<int:pk>/update/",
        WorkCommitmentsUpdateView.as_view(),
        name="work-commitments-update"
    ),
    path(
        "work-commitments/<int:pk>/delete/",
        WorkCommitmentsDeleteView.as_view(),
        name="work-commitments-delete"
    ),
    path(
        "workman/",
        WorkmanListView.as_view(),
        name="workman-list"
    ),
    path(
        "workman/<int:pk>/",
        WorkmanDetailView.as_view(),
        name="workman-detail"
    ),
    path(
        "workman/create/",
        WorkmanCreateView.as_view(),
        name="workman-create"
    ),
    path(
        "workman/<int:pk>/update/",
        WorkmanUpdateView.as_view(),
        name="workman-update"
    ),
    path(
        "workman/<int:pk>/delete/",
        WorkmanDeleteView.as_view(),
        name="workman-delete"
    ),
]

app_name = "hall"
