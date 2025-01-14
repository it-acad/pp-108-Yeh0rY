"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import home_view
from user import views as user_views
from order import views as order_views
from author import views as author_views

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('auth/', include('authentication.urls')),

    # Users URLs
    path('users/', user_views.users_list, name='users_list'),
    path('users/<int:user_id>/', user_views.user_detail, name='user_detail'),

    # Orders URLs
    path('orders/', order_views.orders_list, name='orders_list'),
    path('orders/create/', order_views.create_order, name='create_order'),
    path('orders/my/', order_views.user_orders, name='user_orders'),
    path('orders/close/<int:order_id>/', order_views.close_order, name='close_order'),

    # Authors URLs
    path('authors/', author_views.authors_list, name='authors_list'),
    path('authors/create/', author_views.create_author, name='create_author'),
    path('authors/delete/<int:author_id>/', author_views.delete_author, name='delete_author'),
]
