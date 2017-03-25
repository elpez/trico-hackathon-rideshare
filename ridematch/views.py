from django.shortcuts import render
from django.http import HttpResponseRedirect

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
        time = form.cleaned_data['time']
        day = form.cleaned_data['day']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        if typ == 'D':
            obj = DriverEvent(name=name, destination=dest, time=time, day=day, email=email,
                              phone=phone)
        else:
            obj = PassengerEvent(name=name, destination=dest, time=time, day=day, email=email,
                                 phone=phone)
        obj.save()
        return HttpResponseRedirect('/')
    return render(request, 'ridematch/index.html', {'form':form})

def index_as_get(request):
    form = RideshareForm()
    return render(request, 'ridematch/index.html', {'form':form})
