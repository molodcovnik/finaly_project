from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import TechnicalManualForm, EngineManualForm, TransmissionManualForm, DrivingBridgeManualForm, \
    SteeredBridgeManualForm, MaintenanceManualForm, FailureManualForm, RecoveryManualForm
from .models import *
from accounts.models import ClientUser
from django.http import HttpResponse
from django.template import loader
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


def get_manuals(request):
    tech_list = ModelEquipment.objects.all()
    engine_list = ModelEngine.objects.all()
    transmission_list = ModelTransmission.objects.all()
    steered_bridges_list = ModelSteeredBridge.objects.all()
    driving_bridges_list = ModelDrivingBridge.objects.all()
    maintenance_list = TypeMaintenance.objects.all()
    failure_list = NodeFailure.objects.all()
    methods_list = RecoveryMethod.objects.all()
    template = loader.get_template("manuals/manuals.html")
    context = {
        "technical": tech_list,
        "engines": engine_list,
        "transmissions": transmission_list,
        "steered_bridges": steered_bridges_list,
        "driving_bridges": driving_bridges_list,
        "maintenances": maintenance_list,
        "failures": failure_list,
        "methods": methods_list,
    }
    return HttpResponse(template.render(context, request))

class TechnicalList(ListView):
    model = ModelEquipment
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class TechnicalDetail(DetailView):
    model = ModelEquipment
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_tech_detail', kwargs={'pk': self.get_object().id})


class TechnicalManualCreate(CreateView):
    raise_exception = True
    form_class = TechnicalManualForm
    model = ModelEquipment
    template_name = 'manuals/manual_create.html'


class TechnicalManualUpdate(UpdateView):
    form_class = TechnicalManualForm
    model = ModelEquipment
    template_name = 'manuals/manual_create.html'


class TechnicalManualDelete(DeleteView):
    model = ModelEquipment
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manual_tech_list')


class EngineList(ListView):
    model = ModelEngine
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class EngineDetail(DetailView):
    model = ModelEngine
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_engine_detail', kwargs={'pk': self.get_object().id})


class EngineManualCreate(CreateView):
    raise_exception = True
    form_class = EngineManualForm
    model = ModelEngine
    template_name = 'manuals/manual_create.html'


class EngineManualUpdate(UpdateView):
    form_class = EngineManualForm
    model = ModelEngine
    template_name = 'manuals/manual_create.html'


class EngineManualDelete(DeleteView):
    model = ModelEngine
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manuals')


class TransmissionList(ListView):
    model = ModelTransmission
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class TransmissionDetail(DetailView):
    model = ModelTransmission
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_transmission_detail', kwargs={'pk': self.get_object().id})


class TransmissionManualCreate(CreateView):
    raise_exception = True
    form_class = TransmissionManualForm
    model = ModelTransmission
    template_name = 'manuals/manual_create.html'


class TransmissionManualUpdate(UpdateView):
    form_class = TransmissionManualForm
    model = ModelTransmission
    template_name = 'manuals/manual_create.html'


class TransmissionManualDelete(DeleteView):
    model = ModelTransmission
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manuals')


class DrivingBridgeList(ListView):
    model = ModelDrivingBridge
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class DrivingBridgeDetail(DetailView):
    model = ModelDrivingBridge
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_driving_bridge_detail', kwargs={'pk': self.get_object().id})


class DrivingBridgeManualCreate(CreateView):
    raise_exception = True
    form_class = DrivingBridgeManualForm
    model = ModelDrivingBridge
    template_name = 'manuals/manual_create.html'


class DrivingBridgeManualUpdate(UpdateView):
    form_class = DrivingBridgeManualForm
    model = ModelDrivingBridge
    template_name = 'manuals/manual_create.html'


class DrivingBridgeManualDelete(DeleteView):
    model = ModelDrivingBridge
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manuals')


class SteeredBridgeList(ListView):
    model = ModelSteeredBridge
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class SteeredBridgeDetail(DetailView):
    model = ModelSteeredBridge
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_steered_bridge_detail', kwargs={'pk': self.get_object().id})


class SteeredBridgeManualCreate(CreateView):
    raise_exception = True
    form_class = SteeredBridgeManualForm
    model = ModelSteeredBridge
    template_name = 'manuals/manual_create.html'


class SteeredBridgeManualUpdate(UpdateView):
    form_class = SteeredBridgeManualForm
    model = ModelSteeredBridge
    template_name = 'manuals/manual_create.html'


class SteeredBridgeManualDelete(DeleteView):
    model = ModelSteeredBridge
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manuals')


class MaintenanceList(ListView):
    model = TypeMaintenance
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class MaintenanceDetail(DetailView):
    model = TypeMaintenance
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_maintenance_detail', kwargs={'pk': self.get_object().id})


class MaintenanceManualCreate(CreateView):
    raise_exception = True
    form_class = MaintenanceManualForm
    model = TypeMaintenance
    template_name = 'manuals/manual_create.html'


class MaintenanceManualUpdate(UpdateView):
    form_class = MaintenanceManualForm
    model = TypeMaintenance
    template_name = 'manuals/manual_create.html'


class MaintenanceManualDelete(DeleteView):
    model = TypeMaintenance
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manuals')


class NodeFailureList(ListView):
    model = NodeFailure
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class NodeFailureDetail(DetailView):
    model = NodeFailure
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_node_failure_detail', kwargs={'pk': self.get_object().id})


class NodeFailureManualCreate(CreateView):
    raise_exception = True
    form_class = FailureManualForm
    model = NodeFailure
    template_name = 'manuals/manual_create.html'


class NodeFailureManualUpdate(UpdateView):
    form_class = FailureManualForm
    model = NodeFailure
    template_name = 'manuals/manual_create.html'


class NodeFailureManualDelete(DeleteView):
    model = NodeFailure
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manuals')


class MethodList(ListView):
    model = RecoveryMethod
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'


class MethodDetail(DetailView):
    model = RecoveryMethod
    template_name = 'manuals/manual_detail.html'
    context_object_name = 'manual'

    def get_success_url(self, **kwargs):
        return reverse_lazy('manual_recovery_method_detail', kwargs={'pk': self.get_object().id})


class MethodManualCreate(CreateView):
    raise_exception = True
    form_class = RecoveryManualForm
    model = RecoveryMethod
    template_name = 'manuals/manual_create.html'


class MethodManualUpdate(UpdateView):
    form_class = RecoveryManualForm
    model = RecoveryMethod
    template_name = 'manuals/manual_create.html'


class MethodManualDelete(DeleteView):
    model = RecoveryMethod
    template_name = 'manuals/manual_delete.html'
    success_url = reverse_lazy('manuals')


class ServiceList(ListView):
    model = ClientUser
    template_name = 'manuals/manual.html'
    context_object_name = 'manual'