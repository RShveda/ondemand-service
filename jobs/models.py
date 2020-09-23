from django.db import models
from accounts.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)

    # def get_absolute_url(self):
    #     return reverse("jobs:categories", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True, related_name="jobs")
    location = models.CharField(max_length=100, blank=True, null=True)
    reward = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name="created_jobs")
    assignee = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name="assigned_jobs")
    status = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_status(self, status):
        self.status = status
        status_comment = Comment.objects.create(related_status=status, job=self)
        status_comment.save()
        self.save()
        return status_comment


    def assign(self):
        pass

    def un_assign(self):
        pass

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.TextField()
    job = models.ForeignKey(Job, on_delete=CASCADE, related_name="tasks")
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Comment(models.Model):
    text = models.TextField(blank=True, null=True)
    related_status = models.CharField(max_length=80)
    job = models.ForeignKey(Job, on_delete=CASCADE, related_name="messages")
    author = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_message(self, user, text):
        self.author = str(user)
        self.text = text
        self.save()

    def __str__(self):
        return self.text
