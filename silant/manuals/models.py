from django.db import models


class ModelEquipment(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class ModelEngine(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class ModelTransmission(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class ModelSteeredBridge(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class ModelDrivingBridge(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class TypeMaintenance(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class NodeFailure(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class RecoveryMethod(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'

