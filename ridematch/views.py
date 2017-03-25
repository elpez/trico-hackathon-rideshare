from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RideshareForm

def index(request):
    if request.method == 'POST':
        form = RideshareForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = RideshareForm()
    return render(request, 'ridematch/index.html', {'form':form})
