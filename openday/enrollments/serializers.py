from rest_framework import serializers

from openday.enrollments.models import Enrollment, Event


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = ['uuid', 'event', 'created']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['name', 'when', 'location', 'description',
                  'max_enrollments', 'num_enrollments', 'created']
