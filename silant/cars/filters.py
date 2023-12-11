from django_filters import FilterSet, ChoiceFilter, ModelChoiceFilter, CharFilter
from .models import Machine, Maintenance
from accounts.models import ClientUser
from manuals.models import ModelEquipment, ModelEngine, ModelTransmission, ModelDrivingBridge, ModelSteeredBridge, \
    TypeMaintenance, NodeFailure, RecoveryMethod


class MachineFilter(FilterSet):
    model_technique = ModelChoiceFilter(
        field_name='model_technique',
        queryset=ModelEquipment.objects.all(),
        label='Модель техники',
    )

    model_engine = ModelChoiceFilter(
        field_name='model_engine',
        queryset=ModelEngine.objects.all(),
        label='Модель двигателя',
    )

    model_transmission = ModelChoiceFilter(
        field_name='model_transmission',
        queryset=ModelTransmission.objects.all(),
        label='Модель трансмиссии',
    )

    model_driving_bridge = ModelChoiceFilter(
        field_name='model_driving_bridge',
        queryset=ModelDrivingBridge.objects.all(),
        label='Модель ведущего моста',
    )

    model_steered_bridge = ModelChoiceFilter(
        field_name='model_steered_bridge',
        queryset=ModelSteeredBridge.objects.all(),
        label='Модель управляемого моста',
    )


class MaintenanceFilter(FilterSet):
    machine = CharFilter(
        field_name='machine__serial_number_technique',
        lookup_expr='icontains',
        label='Зав. № машины')

    maintenance_type = ModelChoiceFilter(
        field_name='maintenance_type',
        queryset=TypeMaintenance.objects.all(),
        label='Вид ТО')

    service_company = ModelChoiceFilter(
        field_name='service_company',
        queryset=ClientUser.objects.filter(status='SERVICE'),
        label='Сервисная компания')


class MaintenanceFilterForService(FilterSet):
    machine = CharFilter(
        field_name='machine__serial_number_technique',
        lookup_expr='icontains',
        label='Зав. № машины')

    maintenance_type = ModelChoiceFilter(
        field_name='maintenance_type',
        queryset=TypeMaintenance.objects.all(),
        label='Вид ТО')


class ClaimsFilter(FilterSet):
    node_failure = ModelChoiceFilter(
        field_name='node_failure',
        queryset=NodeFailure.objects.all(),
        label='Узел отказа'
    )

    recovery_method = ModelChoiceFilter(
        field_name='recovery_method',
        queryset=RecoveryMethod.objects.all(),
        label='Способ восстановления'
    )

    service_company_two = ModelChoiceFilter(
        field_name='machine__service_company',
        queryset=ClientUser.objects.filter(status='SERVICE'),
        label='Сервисная компания'
    )