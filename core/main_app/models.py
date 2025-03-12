from django.db import models
from slugify import slugify


class AboutMe(models.Model):
    profile_image = models.ImageField(
        upload_to="images/", blank=True, null=True, help_text="Profil rasmi")
    experience = models.TextField(blank=True, null=True, help_text="Tajriba yoki loyihalar haqida ma'lumot")
    additional_info = models.TextField(blank=True, null=True, help_text="Qo'shimcha ma'lumotlar")


    def __str__(self):
        return "About Me Section"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    text = models.TextField(help_text="Qisqacha tarif")
    title = models.CharField(max_length=100, help_text="Asosiy sarlavha")
    image = models.ImageField(upload_to="images/")
    additional_text = models.TextField(
        blank=True, null=True, help_text="Qo'shimcha matn yoki ma'lumot"
    )
    link = models.URLField(blank=True, null=True, help_text="link")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="portfolios",
        help_text="Portfolio kategoriyasi",
    )  # Category bilan bog'lash
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=5000, help_text="Post yozing")
    image = models.ImageField(upload_to="images/", help_text="Rasmni yuklang")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Contact(models.Model):
    fullname = models.CharField(max_length=100, help_text="Ismingini kiriting")
    email = models.EmailField(help_text="Email manzilingiz")
    phone = models.CharField(max_length=25, help_text="Telefon raqami")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fullname} {self.email}"
