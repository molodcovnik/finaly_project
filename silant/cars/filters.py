from django_filters import FilterSet, ChoiceFilter, ModelChoiceFilter
from .models import Machine
from manuals.models import ModelEquipment, ModelEngine, ModelTransmission, ModelDrivingBridge, ModelSteeredBridge


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
