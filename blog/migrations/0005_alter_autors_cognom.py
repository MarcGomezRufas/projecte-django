# Generated by Django 5.2.1 on 2025-05-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autors',
            name='cognom',
            field=models.CharField(),
        ),
    ]
