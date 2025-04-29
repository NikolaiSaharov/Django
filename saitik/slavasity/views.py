from django.shortcuts import render

def info_view(request):
    return render(request, 'info.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def find_us_view(request):
    return render(request, 'find_us.html')

def products_view(request):
    return render(request, 'products.html')

def categories_view(request):
    return render(request, 'categories.html')

def all_products_view(request):
    return render(request, 'all_products.html')

def cart_view(request):
    return render(request, 'cart.html')