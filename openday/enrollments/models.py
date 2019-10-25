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

    def __str__(self):
        return '{0} on {1} {2} at {3}'.format(self.name,
                                              self.when.date(),
                                              self.when.time(),
                                              self.location)

    def increase_enrollments(self):
        self.num_enrollments += 1
        self.save()

    def has_enroll_spots(self):
        return self.max_enrollments > self.num_enrollments


class Enrollment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} to {1}'.format(self.email, self.event.name)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'event'],
                                    name='unique-enrollment')
        ]
