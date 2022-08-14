from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from meal_plans.models import MealPlan


class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "mealplans/list.html"
    paginate_by = 2

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "mealplans/create.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy("")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("detail_plan", pk=plan.id)


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "mealplans/detail.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "mealplans/edit.html"
    fields = ["name", "date", "recipes"]

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("detail_plan", args=[self.object.pk])


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "mealplans/delete.html"
    success_url = reverse_lazy("meal_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
