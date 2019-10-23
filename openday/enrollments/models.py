import uuid
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    when = models.DateTimeField()
    location = models.CharField(max_length=300)
    description = models.TextField(default='No description available')
    max_enrollments = models.IntegerField(default=0)
    num_enrollments = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)


class Enrollment(models.Model):
    """
    UUID is the User PK or it will be generated (if not logged in) and the
    client will create a QR Code with it
    """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
