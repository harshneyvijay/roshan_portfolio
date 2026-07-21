from django.contrib import admin


admin.site.site_header = "Portfolio Dashboard"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage Your Portfolio"

from .models import (
    Project,
    Education,
    Skill,
    Blog,
    Contact,
    Introduction,
    Document,
    Journey,
    Skill, 
    SkillCategory
)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "show_on_homepage",
    )
    list_editable = (
        "show_on_homepage",
    )
    search_fields = (
        "title",
        "short_description",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "show_on_homepage",
    )
    list_editable = (
        "show_on_homepage",
    )
    search_fields = (
        "title",
        "short_description",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "institution",
        "from_year",
        "to_year",
    )


from .models import Skill, SkillCategory


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    ordering = ("order",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level")
    list_filter = ("category", "level")
    search_fields = ("name",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "document_type",
        "is_active",
        "uploaded_at",
    )
    list_filter = (
        "document_type",
        "is_active",
    )
    search_fields = (
        "title",
    )


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "event_date",
    )
    ordering = (
        "-event_date",
    )
    search_fields = (
        "title",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    pass
