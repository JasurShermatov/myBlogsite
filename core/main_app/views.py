from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden

from .forms import PostForm, ContactForm, PortfolioForm
from .models import AboutMe, Portfolio, Post, Category
from django.shortcuts import get_object_or_404, redirect, HttpResponse
from django.shortcuts import render


def home(request):
    aboutme = AboutMe.objects.all().first()
    portfolios = Portfolio.objects.all()
    posts = Post.objects.all().order_by("-created_at")[:3]
    categories = Category.objects.all()

    portfolios_by_category = {}
    for category in categories:
        portfolios_by_category[category] = Portfolio.objects.filter(category=category)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect("home")
    else:
        form = ContactForm()

    context = {
        "aboutme": aboutme,
        "portfolios": portfolios,
        "posts": posts,
        "categories": categories,
        "portfolios_by_category": portfolios_by_category,
        "form": form,
    }
    return render(request, "home.html", context)


def aboutme(request):
    aboutme_ = AboutMe.objects.prefetch_related("skills").all()
    context = {"aboutme": aboutme_}
    return render(request, "about.html", context)


def portfolio(request):
    categories = Category.objects.all()
    portfolios_by_category = {}

    for category in categories:
        portfolios_by_category[category] = Portfolio.objects.filter(category=category)
    all_portfolios = Portfolio.objects.all()
    context = {
        "categories": categories,
        "portfolios_by_category": portfolios_by_category,
        "all_portfolios": all_portfolios,
    }
    return render(request, "portfolio.html", context)


def post(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {"post": posts}
    return render(request=request, template_name="blog.html", context=context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def add_post(request):
    if not request.user.is_authenticated or not (
        request.user.is_superuser or request.user.is_staff
    ):
        return HttpResponseForbidden("Sizda bu sahifaga kirish huquqi yo'q!")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Post muvaffaqiyatli qo'shildi!")
            return redirect("post")
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, "add-post.html", {"form": form, "posts": posts})


def add_portfolio(request):
    if not request.user.is_authenticated or not (
        request.user.is_superuser or request.user.is_staff
    ):
        return HttpResponseForbidden("Sizda bu sahifaga kirish huquqi yo'q!")

    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)

        if form.is_valid():
            portfolio = form.save(commit=False)

            new_category_name = request.POST.get("new_category")
            if new_category_name:
                new_category, created = Category.objects.get_or_create(
                    name=new_category_name
                )
                portfolio.category = new_category

            portfolio.save()
            messages.success(request, "Portfolio muvaffaqiyatli qo'shildi!")
            return redirect("portfolio")  # Redirect to the portfolio list view
    else:
        form = PortfolioForm()
    categories = Category.objects.all()  # Get all categories
    return render(
        request, "add-portfolio.html", {"form": form, "categories": categories}
    )


def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser)
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post muvaffaqiyatli tahrirlandi!")
            return redirect("post")
    else:
        form = PostForm(instance=post)
    return render(request, "edit_post.html", {"form": form, "post": post})


@user_passes_test(is_superuser)
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Post muvaffaqiyatli o'chirildi!")  # Xabar qo'shildi
    return redirect("post")
