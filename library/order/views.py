# lib/order/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Order
from django.contrib.auth.decorators import login_required, user_passes_test


def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})

# Show orders of the logged-in user (user)
@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/user_order_list.html', {'orders': orders})

@login_required
def create_order(request):
    if request.method == 'POST':
        book = request.POST.get('book')
        order = Order(user=request.user, book=book)
        order.save()
        return redirect('user_orders')  # Redirect to user's orders list
    return render(request, 'order/order_create.html')

def close_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'closed'
    order.save()
    return redirect('orders_list')  # Redirect to orders list
