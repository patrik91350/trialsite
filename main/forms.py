
from .models import City
from django.forms import ModelForm, TextInput, DateTimeInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['country', 'city', 'population', 'short_description', 'date']

        widgets = {
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'population': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Population'
            }),
            'short_description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short_description'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date view yyyy-мм-dd hh:мм'
            }),

        }
