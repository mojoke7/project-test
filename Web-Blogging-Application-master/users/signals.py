from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) # When User is created, send a signal to receiver which will call create_profile()
def create_profile(sender, instance, created, **kwargs): # Receiver passes the user as 'instance'
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
