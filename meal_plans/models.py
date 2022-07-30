from django.conf import settings
from django.db import models

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField()
    owner = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(
        "recipes.Recipe", related_name="meal_plans"
    )
