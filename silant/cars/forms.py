from django import forms
from django.contrib.auth.models import User

from accounts.models import ClientUser
from .models import Machine, Maintenance, Claim


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


class MaintenanceForm(forms.ModelForm):
    machine = forms.ModelChoiceField(queryset=Machine.objects.all())
    service_company = forms.ModelChoiceField(queryset=ClientUser.objects.filter(status='SERVICE'))

    class Meta:
        model = Maintenance
        fields = ['machine', 'maintenance_type', 'service_date', 'operating_time', 'work_order_number',
                  'work_order_date', 'service_company']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Correctly obtains slug from url
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        user_client = User.objects.get(id=user)
        if user_client.is_staff:
            self.fields['machine'].queryset = Machine.objects.all()
        elif user_client.clientuser.status == 'CLIENT':
            self.fields['machine'].queryset = Machine.objects.filter(customer__user=user)
        elif user_client.clientuser.status == 'SERVICE':
            self.fields['machine'].queryset = Machine.objects.all()
            self.fields['service_company'].queryset = ClientUser.objects.filter(user=user)
        elif user_client.clientuser.status == 'MANAGER':
            self.fields['machine'].queryset = Machine.objects.all()


class MaintenanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['maintenance_type', 'service_date', 'operating_time', 'work_order_number',
                  'work_order_date', 'service_company']


class ClaimForm(forms.ModelForm):
    machine = forms.ModelChoiceField(queryset=Machine.objects.all())
    class Meta:
        model = Claim
        fields = ['failure_date', 'operating_time', 'node_failure','description_failure',
                  'recovery_method','spares','restore_date', 'machine', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ClaimForm, self).__init__(*args, **kwargs)
        user_client = User.objects.get(id=user)
        if user_client.is_staff:
            self.fields['machine'].queryset = Machine.objects.all()
        elif user_client.clientuser.status == 'CLIENT':
            self.fields['machine'].queryset = []
        elif user_client.clientuser.status == 'SERVICE':
            self.fields['machine'].queryset = Machine.objects.filter(service_company__user=user)
        elif user_client.clientuser.status == 'MANAGER':
            self.fields['machine'].queryset = Machine.objects.all()


class ClaimUpdateForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['failure_date', 'operating_time', 'node_failure', 'description_failure',
                  'recovery_method', 'spares', 'restore_date', ]
