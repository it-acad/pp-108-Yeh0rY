from django.shortcuts import render, get_object_or_404
from authentication.models import CustomUser  # Import your CustomUser model

# Show all users (for admin/user)
def users_list(request):
    users = CustomUser.get_all()  # Use the method from CustomUser to get all users
    return render(request, 'user/user_list.html', {'users': users})

# Show details for a specific user (for admin/user)
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)  # Use get_by_id to get the user by ID
    return render(request, 'user/user_detail.html', {'user': user})
