from django.shortcuts import render, redirect
from django.views.generic import ListView

from .filters import MachineFilter
from .models import Machine
from .forms import SearchForm


# def index(request):
#     submit_button = request.POST.get("submit")
#     form = SearchForm(request.POST or None)
#     firstname = ''
#     qs = []
#     if form.is_valid():
#         firstname = form.cleaned_data.get("search_field")
#
#     print(firstname)
#     if firstname != '':
#         qs = Machine.objects.filter(serial_number_technique=firstname)
#
#     print(qs)
#     context = {
#         'submit_button': submit_button,
#         'form': form,
#         'f': firstname,
#         'qs': qs,
#     }
#     return render(request, 'cars/cars.html', context)


def index(request):
    if request.user.is_authenticated:
        context = {
            'name': 'Nikolai'
        }
        return render(request, 'cars/cars.html', context)
    else:

        machine_number = ''
        submit_button = request.POST.get("submit")
        form = SearchForm(request.POST or None)
        qs = []
        if form.is_valid():
            machine_number = form.cleaned_data.get("search_field")

        if machine_number != '':
            qs = Machine.objects.filter(serial_number_technique=machine_number)

        print(qs)
        context = {
            'number': machine_number,
            'form': form,
            'submitBtn': submit_button,
            'machines': qs,
        }
        return render(request, 'cars/index_non_auth.html', context)