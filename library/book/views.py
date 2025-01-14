# Create your views here.
from django.shortcuts import render, redirect
from .models import Book
from django.shortcuts import get_object_or_404

def all_books(request):
    books = Book.objects.all()  # Отримати всі книги з бази даних
    return render(request, 'book/all_book.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def filter_books(request):
    books = Book.objects.all()

    # Отримуємо параметри GET-запиту
    title = request.GET.get('title', None)
    if title:
        books = books.filter(name__icontains=title)

    # Видаляємо логіку для фільтрування за автором
    return render(request, 'book/filter_books.html', {'books': books})

def books_by_user(request, user_id):
    if not request.user.is_authenticated or request.user.role != 1:  # Доступ лише для бібліотекаря
        return redirect('login')
    books = Book.objects.filter(borrowed_by__id=user_id)  # Замінити `borrowed_by` на вашу модель
    return render(request, 'book/book_by_user.html', {'books': books})
