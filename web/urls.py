from django.urls import path

from web.views import *

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("saved/", saved_view, name="saved"),
    path("news/add/", news_add_view, name="news_add"),
    path("logout/", logout_view, name="logout"),
    path("news/<int:id>/delete/", news_delete_view, name="news_delete"),
]
