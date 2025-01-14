from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# View для реєстрації
def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        middle_name = request.POST.get("middle_name", "")

        # Отримуємо значення з галочки
        is_librarian = request.POST.get("is_librarian", "off") == "on"

        # Призначаємо роль відповідно до галочки
        role = 1 if is_librarian else 0

        User = get_user_model()

        # Перевірка, чи існує користувач з таким email
        if User.objects.filter(email=email).exists():
            return render(request, "auth/register.html", {"error": "Email already exists."})

        # Створення нового користувача
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            is_active=True,
            role=role  # Передаємо роль бібліотекаря або користувача
        )
        return redirect("login")
    return render(request, "auth/register.html")


# View для логіну
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email: {email}, Password: {password}")

        # Використовуємо email як параметр для authenticate
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("Authentication successful!")
            login(request, user)
            return redirect("/")
        else:
            print("Authentication failed!")
            return render(request, "auth/login.html", {"error": "Invalid email or password"})

    return render(request, "auth/login.html")


# View для логауту
def logout_view(request):
    logout(request)
    return redirect("login")
