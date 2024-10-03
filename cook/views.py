from django.shortcuts import render
from django.views import generic
from cook.models import Cook


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "cook/cook_detail.html"
