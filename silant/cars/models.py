from django.db import models
import datetime

from manuals.models import *
from accounts.models import ClientUser
from manuals.models import *


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

    class Meta:
        ordering = ['-shipment_date']

    def __str__(self):
        return f'{self.model_technique} {self.serial_number_technique} {self.customer.name_company} {self.service_company.name_company}'

    def get_absolute_url(self):
        return reverse('machine_detail', args=[str(self.id)])

    def get_shipment_date(self):
        return (self.shipment_date).strftime("%d.%m.%Y")


class Maintenance(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    maintenance_type = models.ForeignKey(TypeMaintenance, on_delete=models.CASCADE)
    service_date = models.DateField()
    operating_time = models.IntegerField()
    work_order_number = models.CharField(max_length=128)
    work_order_date = models.DateField()
    service_company = models.ForeignKey(ClientUser, on_delete=models.CASCADE,
                                        related_name='maintenances', limit_choices_to={'status': 'SERVICE'},
                                        null=True, blank=True)

    class Meta:
        ordering = ['-service_date']

    def __str__(self):
        return f'{self.machine} {self.maintenance_type} {self.service_date} {self.operating_time} {self.service_company} '

    def get_absolute_url(self):
        return reverse('maintenance_detail', args=[str(self.id)])

    def get_service_date(self):
        return (self.service_date).strftime("%d.%m.%Y")

    def get_work_order_date(self):
        return (self.work_order_date).strftime("%d.%m.%Y")


class Claim(models.Model):
    failure_date = models.DateField()
    operating_time = models.IntegerField()
    node_failure = models.ForeignKey(NodeFailure, on_delete=models.CASCADE)
    description_failure = models.TextField(max_length=2048)
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE)
    spares = models.TextField(max_length=1024, blank=True)
    restore_date = models.DateField(blank=True, null=True)
    downtime = models.IntegerField(blank=True, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.failure_date} {self.operating_time} {self.node_failure} {self.description_failure} {self.recovery_method} {self.spares} {self.restore_date} {self.downtime}'

    @property
    def downtime_machine(self):
        if self.restore_date:
            return (self.restore_date - self.failure_date).days
        return 0

    @property
    def service(self):
        return self.machine.service_company.name_company

    def update_downtime(self):
        self.downtime = (self.restore_date - self.failure_date).days
        self.save()