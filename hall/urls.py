from django.urls import path
from .views import (
    ForemanCreateView,
    ForemanListView,
    ForemanDetailView,
    ForemanUpdateView,
    ForemanDeleteView,
)

from .views import (
    index,
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
]

app_name = "hall"
