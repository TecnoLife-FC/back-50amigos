from django.db import models
from django.utils.translation import gettext_lazy as _

class Dish(models.Model):

    class Meta:
        verbose_name = "platillo"
        verbose_name_plural = "platillos"

    class Category(models.TextChoices):
        STARTER = "ST", "Entradas"
        MAIN_DISH = "MD", "Platos principales"
        DRINKS = "DR", "Bebidas"
        DESSERTS = "DE", "Postres"
        ICE_CREAMS = "IC", "Helados"

    name = models.CharField(_("nombre"), max_length=200)
    cost = models.DecimalField(_("precio"), max_digits=5, decimal_places=2)
    image = models.ImageField(_("imagen"), upload_to="menu/")
    description = models.TextField(_("descripción"))
    category = models.CharField(_("categoria"), max_length=2, choices=Category.choices)
    available = models.BooleanField(_("disponible"))

    def __str__(self):
        return self.name
