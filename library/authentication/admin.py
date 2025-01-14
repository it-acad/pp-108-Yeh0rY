from django.contrib import admin
from .models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'date_of_birth', 'date_of_death', 'get_books')

    search_fields = ('name', 'surname', 'patronymic')

    list_filter = ('books',)

    # Method to display the books associated with the author
    def get_books(self, obj):
        return ", ".join([book.name for book in obj.books.all()])

    get_books.short_description = 'Books'  # Change column name in admin

    list_per_page = 20


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'count', 'get_authors')

    search_fields = ('name', 'description', 'authors__name', 'authors__surname')

    list_filter = ('authors',)

    # Method to display the authors associated with the book
    def get_authors(self, obj):
        return ", ".join([f"{author.name} {author.surname}" for author in obj.authors.all()])

    get_authors.short_description = 'Authors'

    # Organizing the fields into two sections in the form view
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Stock Information', {
            'fields': ('count',),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Book, BookAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('email', 'last_name', 'role')

admin.site.register(CustomUser, CustomUserAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_book_name', 'get_user_email', 'created_at', 'end_at', 'plated_end_at')

    search_fields = ('book__name', 'user__username')

    list_filter = ('book', 'user', 'end_at')

    list_per_page = 20

    # Custom method to display book name in the list view
    def get_book_name(self, obj):
        return obj.book.name

    get_book_name.short_description = 'Book Name'

    # Custom method to display user email in the list view
    def get_user_email(self, obj):
        return obj.user.email

    get_user_email.short_description = 'Email'

    # Order by creation date (descending) to show the most recent orders first
    ordering = ['-created_at']


admin.site.register(Order, OrderAdmin)