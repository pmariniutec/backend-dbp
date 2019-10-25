import uuid

from rest_framework import serializers

from openday.enrollments.models import Enrollment, Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name', 'when', 'location', 'description',
                  'max_enrollments', 'num_enrollments', 'created']


class EnrollmentSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=Event.objects.all())

    class Meta:
        model = Enrollment
        fields = ['id', 'uuid', 'email', 'event', 'event_id']
        read_only_fields = ['id', 'uuid']

    def create(self, validated_data):
        event = validated_data.pop('event_id')
        if event.has_enroll_spots():
            validated_data['event'] = event
            validated_data['uuid'] = uuid.uuid4()
            enrollment = Enrollment.objects.create(**validated_data)
            event.increase_enrollments()

            return enrollment
        else:
            error = {'message': 'No spots available for this event.'}
            raise serializers.ValidationError(error)
