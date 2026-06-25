from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['p_name', 'p_phone', 'p_email', 'doc_name', 'booked_on']
        
        labels = {
            'p_name': 'Patient Name',
            'p_phone': 'Phone Number',
            'p_email': 'Email ID',
            'doc_name': 'Select Doctor',
            'booked_on': 'Booking Date',
        }
        
        widgets = {
            'booked_on': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'p_name': forms.TextInput(attrs={'placeholder': 'Enter full name', 'class': 'form-control'}),
            'p_phone': forms.TextInput(attrs={'placeholder': '10-digit number', 'class': 'form-control'}),
            'p_email': forms.EmailInput(attrs={'placeholder': 'example@mail.com', 'class': 'form-control'}),
            'doc_name': forms.Select(attrs={'class': 'form-control'}),
        }