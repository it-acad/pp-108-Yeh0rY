from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_books, name="all_books"),  # Показати всі книги
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path("filter/", views.filter_books, name="filter_books"),  # Фільтрація книг
    path("user/<int:user_id>/", views.books_by_user, name="books_by_user"),  # Книги для конкретного користувача
]
