from django.db import models
from django.contrib.auth.models import User


class ClientStatusEnum(models.TextChoices):
    CLIENT = 'CLIENT'
    SERVICE = 'SERVICE'
    MANAGER = 'MANAGER'


class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(choices=ClientStatusEnum.choices,
                              default=ClientStatusEnum.CLIENT,
                              max_length=12)
    name_company = models.CharField(max_length=128, blank=True, unique=True)

    def __str__(self):
        return f'{self.user}, {self.status}, {self.name_company}'
