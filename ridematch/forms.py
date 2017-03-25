import datetime
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

one_to_twelve = map(str, range(1, 13))
hour_choices = zip(one_to_twelve, one_to_twelve)
zero_to_fifty_nine = ['00', '15', '30', '45']
min_choices = zip(zero_to_fifty_nine, zero_to_fifty_nine)

current_hour = lambda: datetime.datetime.today().hour

def next_hour():
    hour = current_hour() + 1
    return str(hour - 12) if hour > 12 else str(hour)

def next_meridian():
    """Return the meridian (AM or PM) it will be at the start of the next hour. Used as initial 
       value of field on form.
    """
    return 'PM' if current_hour() + 1 > 12 else 'AM'

def next_day():
    """Return the day it will be at the start of the next hour. Used as initial value of field on 
       form.
    """
    day = datetime.date.today()
    if current_hour() == 23:
        day = datetime.date(day.year, day.month, day.day + 1)
    return day

class RideshareForm(forms.Form):
    name = forms.CharField(label='', initial='Name', max_length=20)
    destination = forms.CharField(label='', initial='Where to?', max_length=50)
    hour = forms.ChoiceField(label='', initial=next_hour, choices=hour_choices)
    minute = forms.ChoiceField(label='', choices=min_choices)
    meridian = forms.ChoiceField(label='', initial=next_meridian, 
                                 choices=[('AM', 'AM'), ('PM', 'PM')])
    day = forms.DateField(label='', initial=next_day, widget=forms.SelectDateWidget)
    email = forms.EmailField(label='', initial='Email')
    phone = forms.CharField(label='', initial='Phone number', max_length=20, required=False)
