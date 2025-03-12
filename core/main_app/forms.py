from django import forms
from .models import Post, Contact, Portfolio, Category


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["fullname", "email", "phone", "description"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "post", "image"]


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["text", "title", "image", "additional_text", "link", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()
