# Generated by Django 4.1.2 on 2022-10-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StatisticData",
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
                ("data_x", models.CharField(max_length=50)),
                ("data_y", models.CharField(max_length=50)),
            ],
        ),
    ]
