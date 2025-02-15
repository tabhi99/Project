# Generated by Django 4.1.4 on 2022-12-15 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=255)),
                ("Blog_Content", models.TextField()),
                (
                    "Create_Date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("Publish_Date", models.DateTimeField(blank=True, null=True)),
                (
                    "Author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
