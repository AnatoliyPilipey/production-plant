from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Foreman(AbstractUser):
    hired_date = models.DateField()
    salary = models.DecimalField()
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} ({self.last_name}, {self.hired_date})"


class WorkCommitments(models.Model):
    duties = models.CharField(max_length=255)
    price = models.FloatField()


class Workmen(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    rate = models.FloatField()
    commitment = models.ForeignKey(
        WorkCommitments,
        on_delete=models.DO_NOTHING,
        related_name="work_commitment"
    )
