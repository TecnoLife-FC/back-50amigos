from django.urls import path

from . import views

app_name = "menus"
urlpatterns = [
    path("", views.MenuView.as_view(), name="item"),
]
