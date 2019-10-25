from django.contrib import admin

from .models import Event, Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'email', 'event', 'created', 'modified']
    fields = ['email', 'event']
    readonly_fields = ['uuid', 'created', 'modified']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'when', 'location', 'description',
                    'max_enrollments', 'num_enrollments', 'created']
    fields = ['name', 'when', 'location', 'description',
              'max_enrollments', 'num_enrollments']
