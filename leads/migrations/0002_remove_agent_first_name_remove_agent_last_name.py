# Generated by Django 4.2.3 on 2023-07-07 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="agent",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="agent",
            name="last_name",
        ),
    ]
