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
            if hour == 12:
                hour = 23
            else:
                hour += 12
        date = datetime.datetime(day.year, day.month, day.day, hour, minute)
        if mode == 'sharer':
            obj = DriverEvent(name=name, destination=dest, date=date, email=email, phone=phone)
            for passenger in active_passengers():
                if check_for_match(passenger, obj):
                    break
        else:
            obj = PassengerEvent(name=name, destination=dest, date=date, email=email, phone=phone)
            for driver in active_drivers():
                if check_for_match(obj, driver):
                    break
        obj.save()
        return HttpResponseRedirect('/thanks')
    context = {'form':form}
    update_context(context, mode)
    return render(request, 'ridematch/tab_form.html', context)

def finder_sharer_as_get(request, mode):
    form = RideshareForm()
    context = {'form':form}
    update_context(context, mode)
    return render(request, 'ridematch/tab_form.html', context)

def update_context(context, mode):
    if mode == 'finder':
        context['table_title'] = 'Drivers Available'
        context['form_title'] = 'Make a Post for a Ride'
        context['obj_list'] = active_drivers()
    else:
        context['table_title'] = 'Passengers Looking for Rides'
        context['form_title'] = 'Offer Your Availability'
        context['obj_list'] = active_passengers()

def active_passengers():
    return PassengerEvent.objects.exclude(date__lt=datetime.datetime.today())

def active_drivers():
    return DriverEvent.objects.exclude(date__lt=datetime.datetime.today())

def same_day(date1, date2):
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

def check_for_match(passenger, driver):
    if passenger.destination.lower() == driver.destination.lower() and \
       same_day(passenger.date, driver.date):
        date_str = driver.date.strftime('%A %m/%d/%y at %I:%M %p')
        send_mail(email_subject, email_body.format(driver, date_str), 'ianfisher45@gmail.com', 
                  [passenger.email])
        return True
    return False

# details for auto-generated email
email_subject = '[Have A Ride] You have a matching ride'
email_body = """\
{0.name} is also driving to {0.destination}.

They are leaving at {1}.
"""
