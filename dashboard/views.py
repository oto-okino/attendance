from django.shortcuts import render

from attendance.models import AttendanceEvent

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")

# def get_status(request):
#     attendance_events = AttendanceEvent.objects.filter(user=request.user, )
#         return render(request, "attendance/test.html", {"attendance_events": attendance_events})