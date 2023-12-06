from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.exceptions import PermissionDenied
from .filters import MachineFilter
from .models import Machine
from .forms import SearchForm, MachineForm


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
        # machine_filters = MachineFilter(request.GET, queryset=machines)
        user = request.user
        if user.is_staff:
            machines = Machine.objects.all()
            machine_filters = MachineFilter(request.GET, queryset=machines)
        elif user.clientuser.status == 'CLIENT':
            machines = Machine.objects.filter(customer__user=user)
            machine_filters = MachineFilter(request.GET, queryset=machines)
        elif user.clientuser.status == 'SERVICE':
            machines = Machine.objects.filter(service_company__user=user)
            machine_filters = MachineFilter(request.GET, queryset=machines)
        elif user.clientuser.status == 'MANAGER':
            machines = Machine.objects.all()
            machine_filters = MachineFilter(request.GET, queryset=machines)

        context = {
            'form': machine_filters.form,
            'machines': machine_filters.qs,
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


class MachinesList(ListView):
    model = Machine
    # queryset = Machine.objects.all()
    template_name = 'cars/machines.html'
    context_object_name = 'machines'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            qs = Machine.objects.all()
        elif user.clientuser.status == 'CLIENT':
            qs = Machine.objects.filter(customer__user=user)
        elif user.clientuser.status == 'SERVICE':
            qs = Machine.objects.filter(service_company__user=user)
        elif user.clientuser.status == 'MANAGER':
            qs = Machine.objects.all()
        return qs

class MachineDetail(DetailView):
    model = Machine
    template_name = 'cars/machine_detail.html'
    context_object_name = 'car'

    def get_success_url(self, **kwargs):
        return reverse_lazy('machine_detail', kwargs={'pk': self.get_object().id})


class MachineCreate(CreateView):
    raise_exception = True
    form_class = MachineForm
    model = Machine
    template_name = 'cars/machine_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        users = User.objects.filter(Q(clientuser__status='MANAGER') | Q(is_staff=True))
        if self.request.user not in users:
            raise PermissionDenied
        return kwargs


class MachineUpdate(UpdateView):
    form_class = MachineForm
    model = Machine
    template_name = 'cars/machine_update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        users = User.objects.filter(Q(clientuser__status='MANAGER') | Q(is_staff=True))
        if self.request.user not in users:
            raise PermissionDenied
        return kwargs


class MachineDelete(DeleteView):
    model = Machine
    template_name = 'cars/machine_delete.html'
    success_url = reverse_lazy('machine_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        users = User.objects.filter(Q(clientuser__status='MANAGER') | Q(is_staff=True))
        if self.request.user not in users:
            raise PermissionDenied
        return kwargs

