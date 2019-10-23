import uuid
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from openday.enrollments.models import Event
from openday.enrollments.serializers import (EnrollmentSerializer,
                                             EventSerializer)


class EnrollUserView(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = EnrollmentSerializer

    def post(self, request, *args, **kwargs):
        request.data.setdefault('uuid', uuid.uuid4())

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data)
        return Response(serializer.data)
