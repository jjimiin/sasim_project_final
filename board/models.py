from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

# 공지
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# 1:1
class Contact_Post(models.Model):
    title = models.CharField(max_length=200)
    mb_id = models.CharField(max_length=20)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    reply = models.TextField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# 1:1
class Contact_Contact(models.Model):
    title = models.CharField(max_length=200)
    mb_id = models.CharField(max_length=20)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    reply = models.TextField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title