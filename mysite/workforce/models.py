from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Team(models.Model):
    teamName = models.CharField(max_length=20)

    def __str__(self):
        return self.teamName


class Member(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    firstname = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50, blank=True)
    city = models.CharField(max_length=20, default="London")
    image = models.ImageField(null=True, blank=True, default="/static/images/default_profile.jpg")
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title


class Upload(models.Model):
    title = models.CharField(max_length=250)
    upload = models.FileField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Deliverables(models.Model):
    title = models.CharField(max_length=250)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    complete = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    upload = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_created=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content


class Work(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    template = models.BooleanField(default=False)

    def __str__(self):
        return self.title
