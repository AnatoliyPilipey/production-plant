from django.urls import path
from .views import (
    ForemanCreateView,
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
    )
]

app_name = "hall"
