from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import JsonResponse

from .models import AttendanceEvent
from .services import get_attendance_status


@login_required
def attendance_view(request):
    attendance_events = AttendanceEvent.objects.filter(user=request.user).order_by("-occurred_at")[:10]
    return render(request, "attendance/test.html", {"attendance_events": attendance_events})

@login_required
def event_create_view(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST で送信してください")
    
    event_type=request.POST.get("event_type")
    current_attendance_status = get_attendance_status(request.user)

    allowed_event_type = {
        AttendanceEvent.EventType.CLOCK_IN,
        AttendanceEvent.EventType.CLOCK_OUT,
    }

    if event_type not in allowed_event_type:
        return HttpResponseBadRequest("不正な打刻です")

    if (event_type == AttendanceEvent.EventType.CLOCK_IN and current_attendance_status != "off_duty"):
        return HttpResponseBadRequest("すでに出勤しています")

    if (event_type == AttendanceEvent.EventType.CLOCK_OUT and current_attendance_status != "working"):
        return HttpResponseBadRequest("現在は出勤していません")

    AttendanceEvent.objects.create(
        user=request.user,
        event_type=event_type,
        occurred_at=timezone.now(),
    )

    return redirect("attendance")

@login_required
def attendance_status_api(request):
    status = get_attendance_status(request.user)

    return JsonResponse({
        "user": request.user.username,
        "status": status,
        "is_working": status == "working",
    })
