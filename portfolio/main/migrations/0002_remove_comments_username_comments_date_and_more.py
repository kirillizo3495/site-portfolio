# Generated by Django 4.2.8 on 2023-12-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='userName',
        ),
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default='14-12-2023', verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='comments',
            name='username',
            field=models.CharField(default=-2021, max_length=100, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
