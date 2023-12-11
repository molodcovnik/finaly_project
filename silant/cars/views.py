from itertools import chain

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.exceptions import PermissionDenied
from .filters import MachineFilter, MaintenanceFilter, MaintenanceFilterForService, ClaimsFilter
from .models import Machine, Maintenance, Claim
from .forms import SearchForm, MachineForm, MaintenanceForm, MaintenanceUpdateForm, ClaimForm, ClaimUpdateForm


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

        if user.is_staff:
            maintenances = Maintenance.objects.all()
            maintenance_filters = MaintenanceFilter(request.GET, queryset=maintenances)
        elif user.clientuser.status == 'CLIENT':
            maintenances = Maintenance.objects.filter(machine__customer__user=user)
            maintenance_filters = MaintenanceFilter(request.GET, queryset=maintenances)
        elif user.clientuser.status == 'SERVICE':
            maintenances = Maintenance.objects.filter(service_company__user=user)
            maintenance_filters = MaintenanceFilterForService(request.GET, queryset=maintenances)
        elif user.clientuser.status == 'MANAGER':
            maintenances = Maintenance.objects.all()
            maintenance_filters = MaintenanceFilter(request.GET, queryset=maintenances)

        if user.is_staff:
            claims = Claim.objects.all()
            claim_filters = ClaimsFilter(request.GET, queryset=claims)
        elif user.clientuser.status == 'CLIENT':
            claims = Claim.objects.filter(machine__customer__user=user)
            claim_filters = ClaimsFilter(request.GET, queryset=claims)
        elif user.clientuser.status == 'SERVICE':
            claims = Claim.objects.filter(machine__service_company__user=user)
            claim_filters = ClaimsFilter(request.GET, queryset=claims)
        elif user.clientuser.status == 'MANAGER':
            claims = Claim.objects.all()
            claim_filters = ClaimsFilter(request.GET, queryset=claims)

        context = {
            'form_machine': machine_filters.form,
            'machines': machine_filters.qs,
            'form_maintenance': maintenance_filters.form,
            'maintenances': maintenance_filters.qs,
            'form_claim': claim_filters.form,
            'claims': claim_filters.qs,
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


class MachinesList(ListView, LoginRequiredMixin):
    model = Machine
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        print(user.id)
        machine = Machine.objects.filter(id=self.kwargs['pk'])
        customer = machine.values_list('customer__user', flat=True)
        service = machine.values_list('service_company__user', flat=True)
        admins = User.objects.filter(is_staff=True).values_list('id', flat=True)
        managers = User.objects.filter(clientuser__status='MANAGER').values_list('id', flat=True)
        access_list = list(chain(customer, service, admins, managers))
        print(access_list)
        if user.id not in access_list:
            raise PermissionDenied
        return context


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


class MaintenanceList(ListView):
    model = Maintenance
    template_name = 'cars/maintenances.html'
    context_object_name = 'maintenances'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            qs = Maintenance.objects.all()
        elif user.clientuser.status == 'CLIENT':
            qs = Maintenance.objects.filter(machine__customer__user=user)
        elif user.clientuser.status == 'SERVICE':
            qs = Maintenance.objects.filter(service_company__user=user)
        elif user.clientuser.status == 'MANAGER':
            qs = Maintenance.objects.all()
        return qs


def get_maintenance_permission(user, pk):
    maintenance = Maintenance.objects.filter(id=pk)
    customer = maintenance.values_list('machine__customer__user', flat=True)
    service = maintenance.values_list('service_company__user', flat=True)
    admins = User.objects.filter(is_staff=True).values_list('id', flat=True)
    managers = User.objects.filter(clientuser__status='MANAGER').values_list('id', flat=True)
    access_list = list(chain(customer, service, admins, managers))
    if user.id in access_list:
        return True
    raise PermissionDenied


class MaintenanceDetail(DetailView):
    model = Maintenance
    template_name = 'cars/maintenance_detail.html'
    context_object_name = 'maintenance'

    def get_success_url(self, **kwargs):
        return reverse_lazy('maintenance_detail', kwargs={'pk': self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        get_maintenance_permission(user, self.kwargs['pk'])
        return context


class MaintenanceCreate(CreateView):
    raise_exception = True
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'cars/maintenance_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        print(kwargs)
        users = User.objects.filter(Q(clientuser__status='MANAGER') | Q(is_staff=True) |
                                    Q(clientuser__status='SERVICE') | Q(clientuser__status='CLIENT'))
        if self.request.user not in users:
            raise PermissionDenied
        return kwargs


class MaintenanceUpdate(UpdateView):
    form_class = MaintenanceUpdateForm
    model = Maintenance
    template_name = 'cars/maintenance_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.machine = self.object.machine
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        get_maintenance_permission(user, self.kwargs['pk'])
        return kwargs


class MaintenanceDelete(DeleteView):
    model = Maintenance
    template_name = 'cars/maintenance_delete.html'
    success_url = reverse_lazy('maintenances_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        print(user.id)
        get_maintenance_permission(user, self.kwargs['pk'])
        return kwargs


class ClaimsList(ListView):
    model = Claim
    template_name = 'cars/claims.html'
    context_object_name = 'claims'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            qs = Claim.objects.all()
        elif user.clientuser.status == 'CLIENT':
            qs = Claim.objects.filter(machine__customer__user=user)
        elif user.clientuser.status == 'SERVICE':
            qs = Claim.objects.filter(machine__service_company__user=user)
        elif user.clientuser.status == 'MANAGER':
            qs = Claim.objects.all()
        return qs


def get_claim_permission_watching(user, pk):
    claim = Claim.objects.filter(id=pk)
    service = claim.values_list('machine__service_company__user', flat=True)
    customer = claim.values_list('machine__customer__user', flat=True)
    admins = User.objects.filter(is_staff=True).values_list('id', flat=True)
    managers = User.objects.filter(clientuser__status='MANAGER').values_list('id', flat=True)
    access_list = list(chain(customer, service, admins, managers))
    if user.id in access_list:
        return True
    raise PermissionDenied


def get_claim_permission(user, pk):
    claim = Claim.objects.filter(id=pk)
    service = claim.values_list('machine__service_company__user', flat=True)
    admins = User.objects.filter(is_staff=True).values_list('id', flat=True)
    managers = User.objects.filter(clientuser__status='MANAGER').values_list('id', flat=True)
    access_list = list(chain(service, admins, managers))
    if user.id in access_list:
        return True
    raise PermissionDenied


class ClaimCreate(CreateView):
    form_class = ClaimForm
    model = Claim
    template_name = 'cars/claim_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        print(kwargs)
        users = User.objects.filter(Q(clientuser__status='MANAGER') | Q(is_staff=True) |
                                    Q(clientuser__status='SERVICE'))
        if self.request.user not in users:
            raise PermissionDenied
        return kwargs

class ClaimDetail(DetailView):
    model = Claim
    template_name = 'cars/claim_detail.html'
    context_object_name = 'claim'

    def get_success_url(self, **kwargs):
        return reverse_lazy('claim_detail', kwargs={'pk': self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        get_claim_permission_watching(user, self.kwargs['pk'])
        return context


class ClaimUpdate(UpdateView):
    form_class = ClaimUpdateForm
    model = Claim
    template_name = 'cars/claim_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.machine = self.object.machine
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        get_claim_permission(user, self.kwargs['pk'])
        return kwargs


class ClaimDelete(DeleteView):
    model = Claim
    template_name = 'cars/claim_delete.html'
    success_url = reverse_lazy('claims_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        get_claim_permission(user, self.kwargs['pk'])
        return kwargs
