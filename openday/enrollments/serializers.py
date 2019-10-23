from rest_framework import serializers

from openday.enrollments.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = ['user']
