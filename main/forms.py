from django import forms

class SearchForm(forms.Form):
    ingredient = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'search-input',
                'class':'form-input-box',
                'autocomplete':'off',
                }
        ),
        label=False
    )

class ConvertForm(forms.Form):
    TEASPOON = "tsp"
    TABLESPOON = 'tbsp'
    CUBIC_INCH = 'in^3'
    FLUID_OUNCE = 'fl oz'
    CUP = 'c'
    PINT = 'pt'
    QUART = 'qt'
    GALLON = 'gal'
    CUBIC_CENTIMETER = 'cm^3'
    GRAM = 'g'

    UNITS = [
        (TEASPOON, 'tsp'),
        (TABLESPOON, 'tbsp'),
        (CUBIC_INCH, 'in^3'),
        (FLUID_OUNCE, 'fl oz'),
        (CUP, 'cup'),
        (PINT, 'pt'),
        (QUART, 'qt'),
        (GALLON, 'gal'),
        (CUBIC_CENTIMETER, 'cm^3'),
    ]

    amount = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-input-box number-input',
                }
        ),
        label=False,
        min_value=0
    )

    unit_from = forms.ChoiceField(
        choices=UNITS,
        widget=forms.Select(
            attrs={
                'class':'choices',
            },
        ),
        label=False
    )

    unit_to = forms.ChoiceField(
        choices=UNITS,
        widget=forms.Select(
            attrs={
                'class':'choices',
            },
        ),
        label=False
    )
