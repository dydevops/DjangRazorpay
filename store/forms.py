from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class OrderPaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','amount',]

    def __init__(self, *args, **kwargs):
        super(OrderPaymentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['amount'].widget.attrs['placeholder'] = 'Amount'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control' 
