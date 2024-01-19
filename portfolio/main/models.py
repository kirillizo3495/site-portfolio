from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import datetime
from django.core.mail import send_mail
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class  Work(models.Model):
    title_work = models.CharField(max_length=50)
    text_work = models.TextField(blank=True)
    img_work = models.ImageField("Фото", upload_to='uplouds_model/%Y/%m/%d/', default=None, blank=True, null=True,)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, db_index=True, blank=True, default='', verbose_name='URL')

    def __str__(self):
        return self.title_work

    def get_absolute_url(self):
        return reverse('work', kwargs={'work_slug': self.slug})


# Create your models here.
