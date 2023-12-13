from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comments(models.Model):
    username = models.CharField('Пользователь',max_length=100)
    comment = models.TextField('Комментарий')
    date = models.DateTimeField('дата публикации', default="2023-12-14 22:59:52")


# Create your models here.
