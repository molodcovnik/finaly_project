from django_filters import FilterSet
from .models import Machine


class MachineFilter(FilterSet):
    class Meta:
        model = Machine

        fields = {
            'serial_number_technique': ['icontains']
        }