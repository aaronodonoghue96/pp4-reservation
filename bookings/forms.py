from django import forms
from .models import Reservation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'number_of_people', 'reservation_time', 'phone_number']

    # Validate number_of_people > 0
    def clean_number_of_people(self):
        number = self.cleaned_data.get('number_of_people')
        if number <= 0:
            raise forms.ValidationError('Number of people must be greater than zero.')
        return number

    def clean_reservation_time(self):
        reservation_time = self.cleaned_data.get('reservation_time')
        # Convert a naive datetime to an aware datetime
        if reservation_time.tzinfo is None:
            reservation_time = timezone.make_aware(reservation_time)
        if reservation_time < timezone.make_aware(datetime.now()):
            raise forms.ValidationError("The selected date cannot be in the past.")
        return reservation_time

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        import re
        pattern = r'^[\d\-\+\s]{7,15}$'
        if not re.match(pattern, phone):
            raise forms.ValidationError('Invalid phone number format.')
        return phone

    def clean(self):
        cleaned_data = super().clean()
        reservation_time = cleaned_data.get('reservation_time')
        phone_number = cleaned_data.get('phone_number')

        if reservation_time and phone_number:
            qs = Reservation.objects.filter(reservation_time=reservation_time, phone_number=phone_number)

            # Exclude self in update case
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise forms.ValidationError('This booking already exists.')

        return cleaned_data

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)