import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .models import DriverEvent, PassengerEvent
from .forms import RideshareForm

def index(request):
    if request.method == 'POST':
        return index_as_post(request)
    else:
        return index_as_get(request)

def index_as_post(request):
    form = RideshareForm(request.POST)
    if form.is_valid():
        typ = form.cleaned_data['d_or_p']
        name = form.cleaned_data['name']
        dest = form.cleaned_data['destination']
        hour = form.cleaned_data['hour']
        minute = form.cleaned_data['minute']
        meridian = form.cleaned_data['meridian']
        day = form.cleaned_data['day']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        # generate time for hour, minute and meridian (AM or PM)
        if meridian == 'PM':
            hour += 12
        time = datetime.time(hour, minute)
        if typ == 'D':
            obj = DriverEvent(name=name, destination=dest, time=time, day=day, email=email,
                              phone=phone)
            for passenger in PassengerEvent.objects.all():
                check_for_match(passenger, obj)
        else:
            obj = PassengerEvent(name=name, destination=dest, time=time, day=day, email=email,
                                 phone=phone)
            for driver in DriverEvent.objects.all():
                check_for_match(obj, driver)
        obj.save()
        return HttpResponseRedirect('/')
    return render(request, 'ridematch/index.html', {'form':form})

def index_as_get(request):
    form = RideshareForm()
    driver_list = DriverEvent.objects.all()
    passenger_list = PassengerEvent.objects.all()
    context = {'form':form, 'driver_list':driver_list, 'passenger_list':passenger_list}
    return render(request, 'ridematch/index.html', context)

def check_for_match(passenger, driver):
    if passenger.destination == driver.destination:
        send_mail(email_subject, email_body.format(driver), 'ianfisher45@gmail.com', 
                  [passenger.email])

# details for auto-generated email
email_subject = '[Have A Ride] You have a matching ride'
email_body = """\
{0.name} is also driving to {0.destination}.

They are leaving at {0.time} on {0.day}.
"""
