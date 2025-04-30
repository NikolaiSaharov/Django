from django import forms
from .models import *

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'price', 'image', 'categories', 'platforms', 'developer', 'publisher', 'release_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'description', 'logo', 'founded_date']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'description', 'logo', 'founded_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'rating', 'comment']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['games', 'total_price', 'status']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['game']
        