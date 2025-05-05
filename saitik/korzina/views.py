from django.contrib import messages
import uuid
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from korzina.forms import *
from korzina.korzina import Korzina
from slavasity.models import Game, PosOrder

def korzina_detail(request):
    korzina = Korzina(request)
    return render(request, 'korzina/detail.html', context={'korzina': korzina})

def korzina_remove(request,product_id):
    korzina = Korzina(request)
    product = get_object_or_404(Game, pk = product_id)
    korzina.remove(product)
    return redirect('korzina_detail')

def korzina_clear(request):
    korzina = Korzina(request)
    korzina.clear()
    return redirect('korzina_detail')

@require_POST
def korzina_add(request, product_id):
    korzina = Korzina(request)
    product = get_object_or_404(Game, pk = product_id)
    form = KorzinaAddProductForm(request.POST)
    if form.is_valid():
        korzina.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=False
        )
    return redirect('korzina_detail')

@login_required
def korzina_buy(request):
    korzina = Korzina(request)
    if korzina.__len__() <= 0:
        return redirect('all_products')
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            user=request.user,
            total_price=korzina.get_total(),
            login_address=form.cleaned_data['login_address'],
            payment_method=form.cleaned_data['payment_method']
        )
        product_ids = [item['product'].id for item in korzina]
        unique_products = Game.objects.filter(id__in=product_ids).distinct()
        order.games.set(unique_products)
        for item in korzina:
                PosOrder.objects.create(
                    order=order,    
                    license_key=str(uuid.uuid4()),
                    delivery_status='delivered'
                )
                korzina.clear()
                messages.success(request, "Заказ успешно оформлен!")
        return redirect('korzina_detail')

@login_required
def open_order(request):
    korzina = Korzina(request)
    context = {
        'form_order': OrderForm,
        'korzina': korzina
    }
    return render(request, 'order/order_form.html', context)