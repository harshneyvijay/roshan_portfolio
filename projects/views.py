from django.shortcuts import render, get_object_or_404
from .models import Document


from .models import (
    Project,
    Education,
    Skill,
    Blog,
    Contact,
    Introduction,
    Document,
)

def project_list(request):

        resumes = Document.objects.filter(
        document_type='resume'
    )

        certificates = Document.objects.filter(
        document_type='certificate'
    )


        return render(
            request,
            'projects/project_list.html',
        {
            'projects': Project.objects.all(),
            'education': Education.objects.all(),
            'skills': Skill.objects.all(),
            'blogs': Blog.objects.all(),
            'contact': Contact.objects.first(),
            'intro': Introduction.objects.first(),
            'resumes':resumes,
            'certificates':certificates,
        }
    )


def project_detail(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk
    )

    return render(
        request,
        'projects/project_detail.html',
        {
            'project': project
        }
    )

def blog_detail(request, pk):

    blog = get_object_or_404(
        Blog,
        pk=pk
    )

    return render(
        request,
        'projects/blog_detail.html',
        {
            'blog': blog
        }
    )

def documents(request):
    docs = Document.objects.all()
    return render(
        request,
        'project_list.html',
        {'documents': docs}
    )