from django.urls import path

from .views import (
    home,
    project_detail,
    blog_detail,
    resume_detail,
    journey,
    projects,
    blogs,
)

urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),

    path(
        "projects/",
        projects,
        name="projects",
    ),

    path(
        "project/<int:pk>/",
        project_detail,
        name="project_detail",
    ),

    path(
        "blogs/",
        blogs,
        name="blogs",
    ),

    path(
        "blog/<int:pk>/",
        blog_detail,
        name="blog_detail",
    ),

    path(
        "resume/<int:pk>/",
        resume_detail,
        name="resume_detail",
    ),

    path(
        "journey/",
        journey,
        name="journey",
    ),
]
