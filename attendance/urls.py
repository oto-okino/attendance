from django.urls import path
from .views import attendance_view, event_create_view, attendance_status_api

urlpatterns = [
    path("", attendance_view, name="attendance"),
    path("event/create/", event_create_view, name="event_create"),
    path("api/status/", attendance_status_api, name="attendance_status_api"),
]