from django.db import models
from django.conf import settings

# Create your models here.
class AttendanceEvent(models.Model):
    class EventType(models.TextChoices):
        CLOCK_IN = "clock_in", "出勤"
        CLOCK_OUT = "clock_out", "退勤"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    occurred_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)