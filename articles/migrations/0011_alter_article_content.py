# Generated by Django 4.1.7 on 2023-04-25 07:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_delete_commentreply_remove_comment_replies_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
