import os
from django.db import models


class Introduction(models.Model):

    name = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()
    
    photo = models.ImageField(upload_to='intro_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)

    short_description = models.TextField()

    full_description = models.TextField()

    technologies = models.CharField(
        max_length=255,
        blank=True
    )

    github_link = models.URLField(
        blank=True
    )

    live_link = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    show_on_homepage = models.BooleanField(
    default=True,
    verbose_name="Show on homepage"
    )

    def __str__(self):
        return self.title
    


class Education(models.Model):
    institution = models.CharField(max_length=200)

    degree = models.CharField(max_length=200)

    from_year = models.IntegerField()

    to_year = models.IntegerField(
        null=True,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return self.institution



class SkillCategory(models.Model):

    name = models.CharField(max_length=100)

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name



class Skill(models.Model):

    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Proficient', 'Proficient'),
    ]


    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills",
        null=True,
        blank=True
    )


    name = models.CharField(max_length=100)


    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='Beginner'
    )


    def __str__(self):
        return f"{self.name} ({self.level})"
    

class Blog(models.Model):

    title = models.CharField(max_length=200)

    short_description = models.TextField()

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    show_on_homepage = models.BooleanField(
    default=True,
    verbose_name="Show on homepage"
    )

    def __str__(self):
        return self.title
        

class Contact(models.Model):

    email = models.EmailField()

    github = models.URLField()

    linkedin = models.URLField()

    twitter = models.URLField(blank=True)

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.email


class Document(models.Model):

    DOCUMENT_TYPES = (
        ('resume', 'Resume'),
        ('certificate', 'Certificate'),
    )

    title = models.CharField(max_length=200, blank=True)
    desc = models.TextField(blank=True)

    document_type = models.CharField(
        max_length=20,
        choices=DOCUMENT_TYPES
    )

    file = models.FileField(upload_to='documents/')

    preview = models.ImageField(
        upload_to='documents/previews/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def extension(self):
        return os.path.splitext(self.file.name)[1].lower()

    @property
    def is_pdf(self):
        return self.extension == ".pdf"

    @property
    def is_image(self):
        return self.extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    

class Journey(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ImageField(upload_to="journey/")
    event_date = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Journey Highlights"
        verbose_name_plural = "Journey Highlights"

    def __str__(self):
        return self.title
