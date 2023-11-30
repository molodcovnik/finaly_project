from django.db import models

from manuals.models import *
from accounts.models import ClientUser


class Machine(models.Model):
    model_technique = models.ForeignKey(ModelEquipment, on_delete=models.CASCADE)
    serial_number_technique = models.CharField(unique=True, max_length=32)
    model_engine = models.ForeignKey(ModelEngine, on_delete=models.CASCADE)
    serial_number_engine = models.CharField(unique=True, max_length=32)
    model_transmission = models.ForeignKey(ModelTransmission, on_delete=models.CASCADE)
    serial_number_transmission = models.CharField(unique=True, max_length=32)
    model_driving_bridge = models.ForeignKey(ModelDrivingBridge, on_delete=models.CASCADE)
    serial_number_driving_bridge = models.CharField(unique=True, max_length=32)
    model_steered_bridge = models.ForeignKey(ModelSteeredBridge, on_delete=models.CASCADE)
    serial_number_steered_bridge = models.CharField(unique=True, max_length=32)
    shipment_date = models.DateField()
    supply_contract = models.CharField(max_length=128, blank=True)
    consignee = models.CharField(max_length=128)
    delivery_address = models.CharField(max_length=256)
    equipment = models.TextField(max_length=5000)
    customer = models.ForeignKey(ClientUser, on_delete=models.CASCADE,related_name='clients', limit_choices_to={'status': 'CLIENT'})
    service_company = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='services', limit_choices_to={'status': 'SERVICE'})

    def __str__(self):
        return f'{self.model_technique} {self.serial_number_technique} {self.model_engine} {self.serial_number_engine} {self.shipment_date} {self.consignee} {self.delivery_address} {self.customer} {self.service_company}'

