from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Claim


@receiver(post_save, sender=Claim)
def create_claims(sender, instance, created, **kwargs):
    if created:
        if instance.restore_date:
            claim = instance
            claim.downtime = instance.downtime_machine
            claim.save()