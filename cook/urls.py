from django.urls import path
from cook.views import CookDetailView, CookUpdateView


urlpatterns = [
    path('profile/<int:pk>', CookDetailView.as_view(), name='profile-detail'),
    path('profile/update/<int:pk>', CookUpdateView.as_view(), name='profile-update')
]

app_name = "cook"