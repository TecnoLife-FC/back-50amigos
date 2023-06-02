from django.shortcuts import render
from django.views import generic

from .models import Dish

class IndexView(generic.ListView):
    template_name = "menu/index.html"
    context_object_name = "dish_list"

    def get_queryset(self):
        return Dish.objects.all().order_by("name")
