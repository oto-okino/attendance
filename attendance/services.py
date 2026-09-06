from .models import AttendanceEvent


def get_attendance_status(user):
    latest_event = AttendanceEvent.objects.filter(user=user).order_by("-occurred_at").first()

    if latest_event is None:
        return "off_duty"

    if latest_event.event_type == AttendanceEvent.EventType.CLOCK_IN:
        return "working"

    if latest_event.event_type == AttendanceEvent.EventType.CLOCK_OUT:
        return "off_duty"

    return "off_duty"