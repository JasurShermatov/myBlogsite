from django.contrib import admin
from .models import AboutMe, Portfolio, Post, Contact, Category


from django.contrib import admin
from .models import AboutMe, ProgrammingSkill


class ProgrammingSkillInline(admin.TabularInline):  # Yoki admin.StackedInline
    model = ProgrammingSkill
    extra = 1  # Qo‘shimcha yangi qator qo‘shadi (ixtiyoriy)
    fields = ("title", "percentage", "experience_since", "image")
    min_num = 0
    max_num = 10  # Maksimum qo‘shish mumkin bo‘lgan skilllar soni


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id")
    fieldsets = (
        ("Asosiy ma'lumotlar", {"fields": ("profile_image",)}),
        ("Matnlar", {"fields": ("experience", "additional_info")}),
    )
    inlines = [ProgrammingSkillInline]  # Inline qo‘shish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "link", "slug")
    list_filter = ("category",)
    search_fields = ("title", "text", "category__name")
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Asosiy ma'lumotlar", {"fields": ("title", "text", "category", "slug")}),
        ("Media", {"fields": ("image",)}),
        (
            "Qo'shimcha ma'lumotlar",
            {"fields": ("additional_text", "link"), "classes": ("collapse",)},
        ),
    )
    list_per_page = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "slug")
    list_filter = ("created_at", "updated_at")
    search_fields = ("title", "post")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created_at"
    fieldsets = (
        ("Post ma'lumotlari", {"fields": ("title", "post", "slug")}),
        ("Media", {"fields": ("image",)}),
    )
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 20


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email", "phone")
    search_fields = ("fullname", "email", "phone", "description")
    list_filter = ("email",)
    fieldsets = (
        ("Bog'lanish ma'lumotlari", {"fields": ("fullname", "email", "phone")}),
        ("Xabar", {"fields": ("description",)}),
    )
    list_per_page = 20
