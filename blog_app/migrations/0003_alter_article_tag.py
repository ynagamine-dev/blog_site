# Generated by Django 3.2.3 on 2021-05-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20210527_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog_app.Tag'),
        ),
    ]
