from django.shortcuts import render
from django.views import generic
from cook.models import Cook
from django.urls import reverse_lazy


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "cook/cook_detail.html"


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = ["years_of_experience","image", "description"]
    
    def get_success_url(self):
        cook_id = self.kwargs.get("pk")
        return reverse_lazy("cook:profile-detail", args=[cook_id])