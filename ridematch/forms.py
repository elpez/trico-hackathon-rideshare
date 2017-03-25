import datetime
from django.core.exceptions import ValidationError
from django import forms

class RideshareForm(forms.Form):
    name = forms.CharField(label='', initial='Name', max_length=20)
    d_or_p = forms.ChoiceField(label='', choices=[('D', 'Driver'), ('P', 'Passenger')])
    destination = forms.CharField(label='', initial='Where to?', max_length=50)
    time = forms.TimeField(label='', initial=datetime.datetime.now().time)
    day = forms.DateField(label='', initial=datetime.date.today)
    email = forms.EmailField(label='', initial='Email')
    phone = forms.CharField(label='', initial='Phone number', max_length=20, required=False)

