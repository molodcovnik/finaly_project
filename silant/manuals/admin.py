from django.contrib import admin
from .models import ModelEquipment, ModelEngine, ModelTransmission, ModelSteeredBridge, ModelDrivingBridge, NodeFailure, TypeMaintenance, RecoveryMethod


admin.site.register(ModelEquipment)
admin.site.register(ModelEngine)
admin.site.register(ModelTransmission)
admin.site.register(ModelSteeredBridge)
admin.site.register(ModelDrivingBridge)
admin.site.register(TypeMaintenance)
admin.site.register(NodeFailure)
admin.site.register(RecoveryMethod)
