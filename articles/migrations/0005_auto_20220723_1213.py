# Generated by Django 3.1.2 on 2022-07-23 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20220723_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parents',
            new_name='parent',
        ),
    ]
