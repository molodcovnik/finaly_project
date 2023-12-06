from django.db import models
from django.urls import reverse


class ModelEquipment(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True, default='Описание техники')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_tech_detail', args=[str(self.id)])

class ModelEngine(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_engine_detail', args=[str(self.id)])


class ModelTransmission(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_transmission_detail', args=[str(self.id)])


class ModelSteeredBridge(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_steered_bridge_detail', args=[str(self.id)])


class ModelDrivingBridge(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_driving_bridge_detail', args=[str(self.id)])


class TypeMaintenance(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_maintenance_detail', args=[str(self.id)])

class NodeFailure(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_node_failure_detail', args=[str(self.id)])


class RecoveryMethod(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('manual_recovery_method_detail', args=[str(self.id)])

