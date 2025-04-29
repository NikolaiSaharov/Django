from django.urls import path
from .views import *

urlpatterns = [
    path('info', info_view, name='info_view'),
    path('about/', about_view, name='about'),
    path('about/contacts/', contact_view, name='contacts'),
    path('about/find-us/', find_us_view, name='find_us'),
    path('products/', products_view, name='products'),
    path('products/categories/', categories_view, name='categories'),
    path('products/all/', all_products_view, name='all_products'),
    path('cart/', cart_view, name='cart'),
]
