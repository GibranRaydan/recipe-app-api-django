from rest_framework import (
    viewsets
)
from task import serializers
from core.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    """View for tasks models"""
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def _string_to_boolean_status(self, status):
        """Convert (pending/completed) in (true/false)"""
        result = False

        if status == 'completed':
            result = True

        return result

    def get_queryset(self):
        status = self.request.query_params.get('status')
        queryset = self.queryset
        if status:
            status = self._string_to_boolean_status(status)
            queryset = queryset.filter(status=status).order_by('-id')

        return queryset
