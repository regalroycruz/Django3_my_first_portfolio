# Generated by Django 3.1.4 on 2020-12-18 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
    ]
