from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class Fault(models.Model):
    """This class represents the bucketlist model."""
    description = models.TextField(blank=False)

    owner = models.ForeignKey('auth.User',
                              related_name='faults',
                              on_delete=models.CASCADE)

    assignee = models.CharField(max_length=255, blank=False)
    item_name = models.CharField(max_length=255, blank=False)
    item_description = models.TextField(blank=False)
    status = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the fault instance."""
        return "{}".format(self.description)


# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
