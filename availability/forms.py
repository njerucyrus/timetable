from django import forms
from django.contrib.auth.models import User
from availability.models import Lecturer

class AvailabilityForm(forms.Form):
    DAYS_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )

    day = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DAYS_CHOICES,
    )

    from_hr = forms.CharField(max_length=10)
    to_hr = forms.CharField(max_length=10)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('phone_number', )


class MessageBroadCastForm(forms.Form):
    message = forms.CharField(max_length=140, widget=forms.Textarea(
        attrs={'id': 'message_id', 'placeholder': 'Write message here'}
    ))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
