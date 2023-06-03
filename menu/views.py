from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from cart.forms import CartAddDishForm
from .models import Dish

class MenuView(generic.ListView):
    template_name = "menu/item.html"
    context_object_name = "dish_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_categories"] = True
        context["cart_dish_form"] = CartAddDishForm()
        return context

    def get_queryset(self):
        return Dish.objects.all().order_by("name")

def db_to_json(request):
    dishes = list(Dish.objects.values())
    data = []
    for item in dishes:
        data.append({
            "model": "menu.Dish",
            "fields": item,
        })
    return JsonResponse(data, safe=False)
