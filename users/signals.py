from django.db import transaction

from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth import get_user_model

from users.models import Profile

User = get_user_model()


@transaction.atomic
@receiver(signals.post_save, sender=User)
def user_post_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
