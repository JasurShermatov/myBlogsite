# Generated by Django 5.1.3 on 2025-02-27 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutMe",
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
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        help_text="Profil rasmi",
                        null=True,
                        upload_to="images/",
                    ),
                ),
                (
                    "experience",
                    models.TextField(
                        blank=True,
                        help_text="Tajriba yoki loyihalar haqida ma'lumot",
                        null=True,
                    ),
                ),
                (
                    "additional_info",
                    models.TextField(
                        blank=True, help_text="Qo'shimcha ma'lumotlar", null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                    "fullname",
                    models.CharField(help_text="Ismingini kiriting", max_length=100),
                ),
                (
                    "email",
                    models.EmailField(help_text="Email manzilingiz", max_length=254),
                ),
                ("phone", models.CharField(help_text="Telefon raqami", max_length=25)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Home",
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
                    models.CharField(help_text="Asosiy sarlavha", max_length=100),
                ),
                (
                    "description",
                    models.TextField(help_text="Saytning qisqacha tavsifi"),
                ),
                (
                    "main_image",
                    models.ImageField(
                        blank=True,
                        help_text="Asosiy rasm",
                        null=True,
                        upload_to="images/",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("post", models.TextField(help_text="Post yozing", max_length=5000)),
                (
                    "image",
                    models.ImageField(help_text="Rasmni yuklang", upload_to="images/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
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
                ("text", models.TextField(help_text="Qisqacha tarif")),
                (
                    "title",
                    models.CharField(help_text="Asosiy sarlavha", max_length=100),
                ),
                ("image", models.ImageField(upload_to="images/")),
                (
                    "additional_text",
                    models.TextField(
                        blank=True, help_text="Qo'shimcha matn yoki ma'lumot", null=True
                    ),
                ),
                ("link", models.URLField(blank=True, help_text="link", null=True)),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Portfolio kategoriyasi",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="portfolios",
                        to="main_app.category",
                    ),
                ),
            ],
        ),
    ]
