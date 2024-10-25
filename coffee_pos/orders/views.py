from django.shortcuts import render, redirect
from .models import Coffee, Order, Receipt

def coffee_list(request):
    coffees = Coffee.objects.all()
    print(coffees)
    return render(request, 'coffee_list.html', {'coffees': coffees})

def create_order(request):
    if request.method == 'POST':
        coffee_id = request.POST.get('coffee_id')
        quantity = int(request.POST.get('quantity'))
        coffee = Coffee.objects.get(id=coffee_id)
        order = Order(coffee=coffee, quantity=quantity)
        order.save()
        receipt = Receipt(order=order)
        receipt.save()
        return redirect('receipt', receipt_id=receipt.id)
    return redirect('coffee_list')

def receipt_detail(request, receipt_id):
    receipt = Receipt.objects.get(id=receipt_id)
    return render(request, 'orders/receipt_detail.html', {'receipt': receipt})