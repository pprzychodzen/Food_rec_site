from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path("register/", views.signup, name="register"),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
]
