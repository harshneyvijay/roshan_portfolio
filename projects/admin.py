from django.contrib import admin
from .models import (
    Project,
    Education,
    Skill,
    Blog,
    Contact,
    Introduction,
    Document,
)

admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Introduction)
admin.site.register(Document)