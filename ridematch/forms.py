import datetime
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

one_to_twelve = map(str, range(1, 13))
hour_choices = zip(one_to_twelve, one_to_twelve)
zero_to_fifty_nine = ['00', '15', '30', '45']
min_choices = zip(zero_to_fifty_nine, zero_to_fifty_nine)

curr_hour = lambda: datetime.datetime.today().hour
curr_meridian = lambda: 'PM' if curr_hour > 12 else 'AM'

class RideshareForm(forms.Form):
    name = forms.CharField(label='', initial='Name', max_length=20)
    destination = forms.CharField(label='', initial='Where to?', max_length=50)
    hour = forms.ChoiceField(label='', initial=curr_hour, choices=hour_choices)
    minute = forms.ChoiceField(label='', choices=min_choices)
    meridian = forms.ChoiceField(label='', initial=curr_meridian, 
                                 choices=[('AM', 'AM'), ('PM', 'PM')])
    day = forms.DateField(label='', initial=datetime.datetime.today, widget=forms.SelectDateWidget)
    email = forms.EmailField(label='', initial='Email')
    phone = forms.CharField(label='', initial='Phone number', max_length=20, required=False)
