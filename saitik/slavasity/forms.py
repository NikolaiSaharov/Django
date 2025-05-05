from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'price', 'image', 'categories', 'platforms', 'developer', 'publisher', 'release_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название игры'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите описание'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Введите цену'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'platforms': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'developer': forms.Select(attrs={'class': 'form-control'}),
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название категории'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание'}),
        }

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название платформы'}),
        }

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'description', 'logo', 'founded_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя разработчика'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'founded_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'description', 'logo', 'founded_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя издателя'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'founded_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'rating', 'comment']
        widgets = {
            'game': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '10', 'placeholder': 'Оценка от 0 до 10'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите комментарий'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['games', 'total_price', 'status']
        widgets = {
            'games': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Введите общую стоимость'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['game']
        widgets = {
            'game': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Почта пользователя',
        min_length=2,
        widget=forms.EmailInput(attrs={'class': 'form-control'})  
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин пользователя', min_length=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput()

