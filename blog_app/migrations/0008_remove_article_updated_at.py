# Generated by Django 3.2.3 on 2021-06-21 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_remove_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
    ]
