from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("meetings/", views.weekly_meetings, name="meetings"),
    path("events/", views.events, name="events"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project-detail"),
]
