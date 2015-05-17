"""
Only enable full updates (PUT). Disable partial updates (PATCH).
"""
from __future__ import unicode_literals
from rest_framework.response import Response


class PutUpdateModelMixin(object):
    """
    Update a model instance via PUT.
    """
    def update(self, request, *args, **kwargs):
        partial = False
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
