from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import CookCreationForm


class SignUpView(generic.CreateView):
    form_class = CookCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("accounts:login")
