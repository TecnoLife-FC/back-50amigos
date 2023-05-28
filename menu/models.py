from django.db import models

class Dish(models.Model):

    class Category(models.TextChoices):
        STARTER = "ST", "Entradas"
        MAIN_DISH = "MD", "Platos principales"
        DRINKS = "DR", "Bebidas"
        DESSERTS = "DE", "Postres"
        ICE_CREAMS = "IC", "Helados"

    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField()
    description = models.TextField()
    category = models.CharField(max_length=2, choices=Category.choices)
    available = models.BooleanField()

    def __str__(self):
        return self.name
