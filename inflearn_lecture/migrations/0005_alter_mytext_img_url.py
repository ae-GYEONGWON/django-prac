# Generated by Django 5.0.2 on 2024-02-27 02:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inflearn_lecture", "0004_mytext_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mytext",
            name="img_url",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]