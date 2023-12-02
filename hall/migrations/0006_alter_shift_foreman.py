# Generated by Django 4.2.3 on 2023-07-18 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0005_alter_workman_commitment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='foreman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='foreman_to_day', to=settings.AUTH_USER_MODEL),
        ),
    ]