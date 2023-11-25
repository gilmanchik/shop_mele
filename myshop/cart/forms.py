from django import forms

PRODUCT_QUANTITY_CHOICE = [(str(i), i) for i in range(1, 21)]


class AddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE, coerce=int)

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)