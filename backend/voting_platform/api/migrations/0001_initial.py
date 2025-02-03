# Generated by Django 5.1.5 on 2025-02-03 19:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "indexes": [
                    models.Index(fields=["name"], name="api_categor_name_53a3ad_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="Nominees",
            fields=[
                (
                    "ID",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.TextField()),
                ("description", models.TextField()),
                ("image", models.URLField(default="NA")),
                ("votes", models.IntegerField(default=0)),
                ("share_link", models.URLField(default="NA")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.category"
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(fields=["name"], name="api_nominee_name_6b4150_idx")
                ],
            },
        ),
    ]
