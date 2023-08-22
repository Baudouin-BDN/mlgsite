# Generated by Django 3.1.2 on 2022-06-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, verbose_name='Contenu')),
                ('photo', models.ImageField(null=True, upload_to='images')),
                ('pub_date', models.DateTimeField(null=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(blank=True, verbose_name='Commentaire')),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.TextField(blank=True, null=True)),
                ('related_comment_id', models.IntegerField(null=True)),
                ('reply_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]