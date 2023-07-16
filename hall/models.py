from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Foreman(AbstractUser):
    hired_date = models.DateField()
    salary = models.DecimalField()
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["first_name"]
        verbose_name = "foreman"
        verbose_name_plural = "foreman"

    def __str__(self):
        return f"{self.first_name} ({self.last_name}, {self.hired_date})"


class WorkCommitments(models.Model):
    duties = models.CharField(max_length=255)
    price = models.FloatField()


class Workman(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    rate = models.FloatField()
    commitment = models.ForeignKey(
        WorkCommitments,
        on_delete=models.SET_NULL,
        related_name="work_commitment"
    )


class Shift(models.Model):
    work_date = models.DateField()
    products_produced = models.FloatField()
    foreman = models.ForeignKey(
        Foreman,
        on_delete=models.SET_NULL,
        related_name="foreman_to_day"
    )
    workman = models.ManyToManyField(
        Workman,
        related_name="workman_to_day"
    )
