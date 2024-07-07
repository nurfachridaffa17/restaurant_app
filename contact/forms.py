from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Purpose',
                'id': 'name',
            },
        ),
        max_length=100
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'id': 'email',
            },
        )
    )
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'id': 'message',
            }
        ),
        max_length=1000
    )
