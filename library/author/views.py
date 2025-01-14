# lib/author/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Author

# Show all authors (admin)
def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors': authors})

# Create a new author (admin)
def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = Author(name=name)
        author.save()
        return redirect('authors_list')
    return render(request, 'author/author_create.html')

# Delete an author (admin)
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    # Only delete if author is not linked to any books
    if not author.books.exists():
        author.delete()
    return redirect('authors_list')
