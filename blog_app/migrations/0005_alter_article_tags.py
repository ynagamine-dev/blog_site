# Generated by Django 3.2.3 on 2021-06-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20210527_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='article_set', to='blog_app.Tag'),
        ),
    ]
