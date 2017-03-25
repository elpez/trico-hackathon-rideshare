import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .models import DriverEvent, PassengerEvent
from .forms import RideshareForm

def index(request):
    return render(request, 'ridematch/index.html')

def thanks(request):
    return render(request, 'ridematch/thanks.html')

def finder_sharer(request, mode):
    if request.method == 'POST':
        return finder_sharer_as_post(request, mode)
    else:
        return finder_sharer_as_get(request, mode)

def finder_sharer_as_post(request, mode):
    form = RideshareForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        dest = form.cleaned_data['destination']
        hour = int(form.cleaned_data['hour'])
        minute = int(form.cleaned_data['minute'])
        meridian = form.cleaned_data['meridian']
        day = form.cleaned_data['day']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        # generate time for hour, minute and meridian (AM or PM)
        if meridian == 'PM':
            hour += 12
        time = datetime.time(hour, minute)
        if mode == 'sharer':
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
        return HttpResponseRedirect('/thanks')
    context = {'form':form}
    update_context(context, mode)
    return render(request, 'ridematch/tab_form.html', context)

def finder_sharer_as_get(request, mode):
    form = RideshareForm()
    driver_list = DriverEvent.objects.all()
    passenger_list = PassengerEvent.objects.all()
    context = {'form':form, 'driver_list':driver_list, 'passenger_list':passenger_list}
    update_context(context, mode)
    return render(request, 'ridematch/tab_form.html', context)

def update_context(context, mode):
    if mode == 'finder':
        context['table_title'] = 'Drivers available'
        context['form_title'] = 'Make a post for a ride'
        context['obj_list'] = DriverEvent.objects.all()
    else:
        context['table_title'] = 'Passengers looking for rides'
        context['form_title'] = 'Offer your availability'
        context['obj_list'] = PassengerEvent.objects.all()

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
