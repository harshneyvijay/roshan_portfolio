from django.shortcuts import render, get_object_or_404
from .models import (
    Project,
    Education,
    Skill,
    SkillCategory,
    Blog,
    Contact,
    Introduction,
    Document,
    Journey,
)

import os

from django.contrib.auth import get_user_model
from django.http import HttpResponse


def create_admin(request):
    User = get_user_model()

    username = os.environ.get("ADMIN_USERNAME")
    password = os.environ.get("ADMIN_PASSWORD")

    if not username or not password:
        return HttpResponse("Admin credentials not configured")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            password=password
        )

        return HttpResponse("Admin created successfully")

    return HttpResponse("Admin already exists")


def home(request):

    resumes = Document.objects.filter(
        document_type="resume",
        is_active=True,
    )

    certificates = Document.objects.filter(
        document_type="certificate"
    )

    return render(
        request,
        "projects/home.html",
        {
            "projects": Project.objects.filter(
                show_on_homepage=True
            ),
            "education": Education.objects.all(),
            "skill_categories": SkillCategory.objects.prefetch_related("skills").all(),
            "blogs": Blog.objects.filter(
                show_on_homepage=True
            ),
            "contact": Contact.objects.first(),
            "intro": Introduction.objects.first(),
            "resumes": resumes,
            "certificates": certificates,
        },
    )


def projects(request):

    return render(
        request,
        "projects/projects.html",
        {
            "projects": Project.objects.all(),
            "intro": Introduction.objects.first(),
        },
    )


def blogs(request):

    return render(
        request,
        "projects/blogs.html",
        {
            "blogs": Blog.objects.all(),
            "intro": Introduction.objects.first(),
        },
    )


def project_detail(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    return render(
        request,
        "projects/project_detail.html",
        {
            "project": project,
            "intro": Introduction.objects.first(),
        },
    )


def blog_detail(request, pk):

    blog = get_object_or_404(
        Blog,
        pk=pk
    )

    return render(
        request,
        "projects/blog_detail.html",
        {
            "blog": blog,
            "intro": Introduction.objects.first(),
        },
    )


def resume_detail(request, pk):

    resume = get_object_or_404(
        Document,
        pk=pk,
        document_type="resume",
    )

    return render(
        request,
        "projects/resume_detail.html",
        {
            "resume": resume,
            "intro": Introduction.objects.first(),
        },
    )


def journey(request):

    journey = Journey.objects.order_by("-event_date")

    return render(
        request,
        "projects/journey.html",
        {
            "journey": journey,
            "intro": Introduction.objects.first(),
        },
    )
