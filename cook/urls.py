from django.urls import path
from cook.views import CookDetailView


urlpatterns = [
    path('profile/<int:pk>', CookDetailView.as_view(), name='profile'),
]

app_name = "cook"