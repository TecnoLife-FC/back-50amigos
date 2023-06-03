from django.urls import path

from . import views

app_name = "menus"
urlpatterns = [
    path("", views.MenuView.as_view(), name="item"),
    path("json/", views.db_to_json, name="json"),
]
