from django import forms

DISH_QUANTIFY_CHOICE = [(i, str(i)) for i in range(1, 21)]

class CartAddDishForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=DISH_QUANTIFY_CHOICE,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial= False,
        widget=forms.HiddenInput
    )
