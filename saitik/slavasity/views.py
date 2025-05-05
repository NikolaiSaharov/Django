from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from korzina.forms import KorzinaAddProductForm
from django.contrib.auth import login, logout
from django.views import View  # Добавлено для наследования

def info_view(request):
    games = Game.objects.all()[:3]  
    return render(request, 'info.html', {'games': games})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def find_us_view(request):
    return render(request, 'find_us.html')

class ProductsView(ListView):
    model = Category
    template_name = 'products.html'
    context_object_name = 'categories'

class CategoriesView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

class AllProductsView(ListView):
    model = Game
    template_name = 'all_products.html'
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = KorzinaAddProductForm()
        return context

def cart_view(request):
    return render(request, 'cart.html')

class GamesListView(ListView):
    model = Game
    template_name = 'games/games_list.html'
    context_object_name = 'games'

class GamesDetailView(DetailView):
    model = Game
    template_name = 'games/games_detail.html'
    context_object_name = 'game'

class GamesCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/games_form.html'
    success_url = reverse_lazy('games_list')

class GamesUpdateView(UpdateView):
    model = Game
    form_class = GameForm
    context_object_name = 'game'
    template_name = 'games/games_form.html'
    success_url = reverse_lazy('games_list')

class GamesDeleteView(DeleteView):
    model = Game
    template_name = 'games/games_delete.html'
    context_object_name = 'game'
    success_url = reverse_lazy('games_list')

class CategoriesListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')

class PlatformsListView(ListView):
    model = Platform
    template_name = 'platform/platform_list.html'
    context_object_name = 'platforms'

class PlatformDetailView(DetailView):
    model = Platform
    template_name = 'platform/platform_detail.html'
    context_object_name = 'platform'

class PlatformCreateView(CreateView):
    model = Platform
    form_class = PlatformForm
    template_name = 'platform/platform_form.html'
    success_url = reverse_lazy('platform_list')

class PlatformUpdateView(UpdateView):
    model = Platform
    form_class = PlatformForm
    template_name = 'platform/platform_form.html'
    success_url = reverse_lazy('platform_list')

class PlatformDeleteView(DeleteView):
    model = Platform
    template_name = 'platform/platform_delete.html'
    context_object_name = 'platform'
    success_url = reverse_lazy('platform_list')

class DevelopersListView(ListView):
    model = Developer
    template_name = 'developer/developer_list.html'
    context_object_name = 'developers'

class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'developer/developer_detail.html'
    context_object_name = 'developer'

class DeveloperCreateView(CreateView):
    model = Developer
    form_class = DeveloperForm
    template_name = 'developer/developer_form.html'
    success_url = reverse_lazy('developer_list')

class DeveloperUpdateView(UpdateView):
    model = Developer
    form_class = DeveloperForm
    template_name = 'developer/developer_form.html'
    success_url = reverse_lazy('developer_list')

class DeveloperDeleteView(DeleteView):
    model = Developer
    template_name = 'developer/developer_delete.html'
    context_object_name = 'developer'
    success_url = reverse_lazy('developer_list')

class PublishersListView(ListView):
    model = Publisher
    template_name = 'publisher/publisher_list.html'
    context_object_name = 'publishers'

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'publisher/publisher_detail.html'
    context_object_name = 'publisher'

class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/publisher_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/publisher_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher/publisher_delete.html'
    context_object_name = 'publisher'
    success_url = reverse_lazy('publisher_list')

class ReviewsListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review_list')

class OrdersListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_delete.html'
    context_object_name = 'order'
    success_url = reverse_lazy('order_list')

class WishlistsListView(ListView):
    model = Wishlist
    template_name = 'wishlist/wishlist_list.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

class WishlistDetailView(DetailView):
    model = Wishlist
    template_name = 'wishlist/wishlist_detail.html'
    context_object_name = 'wishlist'

class WishlistCreateView(CreateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist/wishlist_form.html'
    success_url = reverse_lazy('wishlist_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WishlistUpdateView(UpdateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist/wishlist_form.html'
    success_url = reverse_lazy('wishlist_list')

class WishlistDeleteView(DeleteView):
    model = Wishlist
    template_name = 'wishlist/wishlist_delete.html'
    context_object_name = 'wishlist'
    success_url = reverse_lazy('wishlist_list')

class login_user(View):
    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
        else:
            form = LoginForm()
            context = {'form': form}
            return render(request, 'auth/login.html', context)

    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context)

class register_user(View):
    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
        else:
            context = {'form': form}
            return render(request, 'auth/register.html', context)

    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'auth/register.html', context)

def logout_user(request):
    logout(request)
    return redirect('info_view')