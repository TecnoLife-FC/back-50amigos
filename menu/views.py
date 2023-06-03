from django.shortcuts import render
from django.views import generic

from .models import Dish

class MenuView(generic.ListView):
    template_name = "menu/item.html"
    context_object_name = "dish_list"

    def get_queryset(self):
        return Dish.objects.all().order_by("name")
