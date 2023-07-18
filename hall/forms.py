from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Foreman


class ForemanCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Foreman
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "salary"
        )


class SearchForm(forms.Form):
    value_ = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )
