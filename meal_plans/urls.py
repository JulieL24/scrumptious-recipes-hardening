from django.urls import path

from meal_plans.views import (
    MealPlanListView,
    MealPlanCreateView,
    MealPlanDetailView,
    MealPlanUpdateView,
    MealPlanDeleteView,
)


urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_list"),
    path("create/", MealPlanCreateView.as_view(), name="create_plan"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="detail_plan"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="edit_plan"),
    path("<int:pk>/delete/", MealPlanDeleteView.as_view(), name="delete_plan"),
]
