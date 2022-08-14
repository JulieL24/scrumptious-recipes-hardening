from django import template

register = template.Library()


def resize_to(ingredient, target):
    print("value:", ingredient)
    print("arg:", target)
    # return "resize done"
    # Get the number of servings from the ingredient's
    # recipe using the ingredient.recipe.servings
    # properties
    servings = ingredient.recipe.servings
    if servings is not None and target is not None:
        try:
            ratio = int(target) / servings
            return ingredient.amount * ratio
        except ValueError:
            pass
        return ingredient.amount
    # If the servings from the recipe is not None
    #   and the value of target is not None
    # try
    # calculate the ratio of target over
    #   servings
    # return the ratio multiplied by the
    #   ingredient's amount
    # catch a possible error
    # pass
    # return the original ingredient's amount since
    #   nothing else worked


register.filter(resize_to)
