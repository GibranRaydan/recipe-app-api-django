""" Serializers for Task model"""

from rest_framework import serializers

from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for task view"""
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status']
        read_only_fields = ['id']
