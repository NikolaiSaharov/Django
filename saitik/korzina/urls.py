from django.urls import path
from .views import *

urlpatterns = [
    path('', korzina_detail, name='korzina_detail'),
    path('remove/<int:product_id>/', korzina_remove, name='korzina_remove'),
    path('add/<int:product_id>/', korzina_add, name='korzina_add'),
    path('clear/', korzina_clear, name='korzina_clear'),
    path('buy/', korzina_buy, name='korzina_buy'),
    path('create_order/', open_order, name='open_order'),

]
