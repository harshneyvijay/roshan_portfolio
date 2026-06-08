from django.db import models

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

    def __str__(self):
        return self.title
    


class Education(models.Model):
    institution = models.CharField(max_length=200)

    degree = models.CharField(max_length=200)

    year = models.IntegerField()

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.institution


class Skill(models.Model):

    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Proficient', 'Proficient'),
    ]

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

    def __str__(self):
        return self.title
        

class Contact(models.Model):

    email = models.EmailField()

    github = models.URLField()

    linkedin = models.URLField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.email
    

class Introduction(models.Model):

    name = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    def __str__(self):
        return self.name
    

from django.db import models

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
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title