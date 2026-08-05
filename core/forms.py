from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service_type', 'preferred_date', 'notes']
        widgets = {
            'service_type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'preferred_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about your machine make, model',
            }),
        }
