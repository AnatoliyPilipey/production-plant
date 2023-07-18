from django.db import models
from django.contrib.auth.models import AbstractUser


class Foreman(AbstractUser):
    hired_date = models.DateField(null=True)
    salary = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "foreman"
        verbose_name_plural = "foreman"

    def __str__(self):
        return f"{self.first_name} ({self.last_name}, {self.hired_date})"


class WorkCommitments(models.Model):
    duties = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.duties


class Workman(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    commitment = models.ForeignKey(
        WorkCommitments,
        on_delete=models.SET_NULL,
        related_name="work_commitment",
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Shift(models.Model):
    work_date = models.DateField()
    products_produced = models.DecimalField(max_digits=50, decimal_places=2)
    foreman = models.ForeignKey(
        Foreman,
        on_delete=models.SET_NULL,
        related_name="foreman_to_day",
        null=True
    )
    workman = models.ManyToManyField(
        Workman,
        related_name="workman_to_day"
    )

    def __str__(self):
        return f"Data: {self.work_date} Produced: {self.products_produced}"
