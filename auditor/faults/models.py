from django.db import models


class Fault(models.Model):
    """This class represents the bucketlist model."""
    description = models.TextField(blank=False)
    assignee = models.CharField(max_length=255, blank=False)
    item_name = models.CharField(max_length=255, blank=False)
    item_description = models.TextField(blank=False)
    status = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the fault instance."""
        return "{}".format(self.description)
