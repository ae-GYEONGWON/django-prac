# Generated by Django 5.0.2 on 2024-02-27 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inflearn_lecture", "0005_alter_mytext_img_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("write", models.CharField(max_length=200, null=True)),
                ("rate", models.CharField(max_length=200, null=True)),
                ("comment", models.CharField(max_length=200, null=True)),
                (
                    "lecture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inflearn_lecture.mytext",
                    ),
                ),
            ],
        ),
    ]
