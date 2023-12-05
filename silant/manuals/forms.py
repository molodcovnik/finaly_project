from django import forms
from .models import *
from django.forms import Textarea


class TechnicalManualForm(forms.ModelForm):
    class Meta:
        model = ModelEquipment
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})


class EngineManualForm(forms.ModelForm):
    class Meta:
        model = ModelEngine
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})


class TransmissionManualForm(forms.ModelForm):
    class Meta:
        model = ModelTransmission
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})


class DrivingBridgeManualForm(forms.ModelForm):
    class Meta:
        model = ModelDrivingBridge
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})


class SteeredBridgeManualForm(forms.ModelForm):
    class Meta:
        model = ModelSteeredBridge
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})


class MaintenanceManualForm(forms.ModelForm):
    class Meta:
        model = TypeMaintenance
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})


class FailureManualForm(forms.ModelForm):
    class Meta:
        model = NodeFailure
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})


class RecoveryManualForm(forms.ModelForm):
    class Meta:
        model = RecoveryMethod
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget = Textarea(attrs={'rows': 2})
        self.fields['description'].widget = Textarea(attrs={'rows': 5})