from django.urls import path
from .views import project_list, project_detail, blog_detail, documents

urlpatterns = [
    path('', project_list, name='project_list'),

    path(
        'project/<int:pk>/',
        project_detail,
        name='project_detail'
    ),

    path(
    'blog/<int:pk>/',
    blog_detail,
    name='blog_detail'
),

path(
    'documents/',
    documents,
    name='documents'
),

]