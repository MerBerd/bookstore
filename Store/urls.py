from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newBook", views.newBook, name="newBook"),
    path("newAuthor", views.newAuthor, name="newAuthor"),
    path("book/<int:book_id>", views.book, name="book"),
    path("shoplist", views.shoplist, name="shoplist"),
    path("shoplistChange/<int:book_id>", views.shoplistChange, name="shoplistChange")
]