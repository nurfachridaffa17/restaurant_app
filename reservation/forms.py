from django import forms
from .models import Reservation

class ReserveTableForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    time = forms.TimeField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Your Name'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email Address'
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Phone Number'
            }
        )
    )

    number_of_guests = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'number_of_guests',
                'placeholder': 'Number of Guests'
            }
        )
    )
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'number_of_guests', 'date', 'time']