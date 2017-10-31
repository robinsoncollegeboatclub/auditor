from rest_framework import serializers
from .models import Fault


class FaultSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Fault
        fields = ('id', 'description', 'assignee', 'item_name', 'item_description', 'status', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
