import datetime
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class RideshareForm(forms.Form):
    d_or_p = forms.ChoiceField(label='', choices=[('D', 'Driver'), ('P', 'Passenger')])
    name = forms.CharField(label='', initial='Name', max_length=20)
    destination = forms.CharField(label='', initial='Where to?', max_length=50)
    time = forms.TimeField(label='', initial=datetime.datetime.now().time)
    day = forms.DateField(label='', initial=datetime.date.today, widget=forms.SelectDateWidget)
    email = forms.EmailField(label='', initial='Email')
    phone = forms.CharField(label='', initial='Phone number', max_length=20, required=False)

