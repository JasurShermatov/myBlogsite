from django.urls import path
from .views import home, aboutme, portfolio, post, contact, add_post, add_portfolio, edit_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('aboutme/', aboutme, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('post/', post, name='post'),
    path('contact/', contact, name='contact'),
    path('add_post/', add_post, name='add_post'),
    path('add_portfolio/', add_portfolio, name='add_portfolio'),
    path('post/<slug:slug>/', edit_post, name='edit_post'),  # Tahrirlash uchun URL
    path('post/delete/<slug:slug>/', delete_post, name='delete_post'),  # O'chirish uchun URL
]
