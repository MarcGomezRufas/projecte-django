# Generated by Django 5.2.1 on 2025-05-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(null=True, related_name='posts', to='blog.tag'),
        ),
    ]
