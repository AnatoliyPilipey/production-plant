from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Foreman,
    WorkCommitments,
    Workman,
    Shift
)


@admin.register(Foreman)
class ForemanAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("salary",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("salary",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "salary",
                    )
                },
            ),
        )
    )


@admin.register(WorkCommitments)
class WorkCommitmentsAdmin(admin.ModelAdmin):
    list_display = ["duties", "price"]


@admin.register(Workman)
class WorkmanAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "rate",
        "commitment"
    ]


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = [
        "work_date",
        "products_produced",
        "foreman",
    ]
    list_filter = ["foreman"]
    search_fields = ["work_date"]
