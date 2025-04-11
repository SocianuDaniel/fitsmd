from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from core.models import Owner,OwnerProfile





def createProfile(sender, instance, created, **kwargs):
    if created:
        user = Owner.objects.get(user=instance.user)
        profile = OwnerProfile.objects.create(
            owner=user
        )

post_save.connect(createProfile, sender=Owner)
