from django.urls import path
from .views import (
    ForemanCreateView,
    ForemanListView,
    ForemanDetailView,
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
]

app_name = "hall"
