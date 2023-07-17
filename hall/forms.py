from django.contrib.auth.forms import UserCreationForm

from .models import Foreman


class ForemanCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Foreman
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "salary"
        )
