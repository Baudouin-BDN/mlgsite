# Generated by Django 3.1.2 on 2022-07-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20220723_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(to='articles.Reponse'),
        ),
    ]
