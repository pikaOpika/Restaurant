from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import SignUpView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

app_name = "accounts"
