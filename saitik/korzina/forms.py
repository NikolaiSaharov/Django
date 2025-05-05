from django import forms

from slavasity.models import Order

class KorzinaAddProductForm(forms.Form):
    count = forms.IntegerField(
        min_value=1,max_value=10,initial=1,label="Количество",widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class OrderForm(forms.Form):
    login_address = forms.CharField(max_length=255, label='Адрес доставки', widget=forms.TextInput(attrs={'placeholder': 'Введите адрес'}))
    payment_method = forms.ChoiceField(
        choices=[
            ('card', 'Кредитная карта'),
            ('cash', 'Наличные'),
        ],
        label='Способ оплаты',
        widget=forms.Select()
    )