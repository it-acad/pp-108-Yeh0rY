from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Шлях до login_view
    path('register/', views.register, name='register'),  # Шлях до register
    path('logout/', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),  # Шлях до logout
]
