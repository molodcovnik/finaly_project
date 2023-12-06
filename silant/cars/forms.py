from django import forms

from cars.models import Machine


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_field'].widget.attrs['placeholder'] = 'Зав. № машины'
        self.fields['search_field'].label = ''


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['model_technique', 'serial_number_technique', 'model_engine',
                  'serial_number_engine', 'model_transmission', 'serial_number_transmission',
                  'model_driving_bridge', 'serial_number_driving_bridge', 'model_steered_bridge',
                  'serial_number_steered_bridge', 'shipment_date', 'supply_contract',
                  'consignee', 'delivery_address', 'equipment',
                  'customer', 'service_company', ]
