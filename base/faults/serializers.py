from rest_framework import serializers
from .models import Fault
from django.contrib.auth.models import User


class FaultSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Fault
        fields = ('id', 'description', 'assignee', 'item_name', 'item_description', 'status', 'date_created', 'date_modified', 'owner')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    faults = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Fault.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'bucketlists')
