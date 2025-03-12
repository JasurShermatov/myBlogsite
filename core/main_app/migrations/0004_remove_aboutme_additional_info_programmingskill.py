# Generated by Django 5.1.3 on 2025-03-12 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_delete_home_portfolio_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aboutme",
            name="additional_info",
        ),
        migrations.CreateModel(
            name="ProgrammingSkill",
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
                (
                    "title",
                    models.CharField(
                        help_text="Skill nomi (masalan, Python)", max_length=100
                    ),
                ),
                (
                    "percentage",
                    models.FloatField(help_text="Skill foizi (masalan, 80.0)"),
                ),
                (
                    "experience_since",
                    models.DateField(
                        help_text="Qachondan beri tajriba (masalan, 2023-10-01)"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Skill logosi yoki rasmi",
                        null=True,
                        upload_to="skills/",
                    ),
                ),
                (
                    "about_me",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skills",
                        to="main_app.aboutme",
                    ),
                ),
            ],
        ),
    ]
