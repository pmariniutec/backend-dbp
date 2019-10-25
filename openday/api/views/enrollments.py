from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from openday.enrollments.models import Event, Enrollment
from openday.enrollments.serializers import (EnrollmentSerializer,
                                             EventSerializer)


class EnrollGuestView(APIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(email=self.kwargs['email'])

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnrollUserView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(email=self.request.user.email)

    def get(self, request):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnrollmentDelete(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EnrollmentSerializer

    def delete(self, request, *args, **kwargs):
        try:
            enrollment_id = kwargs.get('id')
            email = request.user.email
            Enrollment.objects.filter(id=enrollment_id, email=email).delete()
            return Response({'status': 'true'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'status': 'error'},
                            status=status.HTTP_404_NOT_FOUND)


class EventView(APIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
