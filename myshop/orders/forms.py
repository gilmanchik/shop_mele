from django import forms
from .models import OrderInfo


class OrderInfoForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
