# Generated by Django 5.0.6 on 2024-06-18 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_alter_post_content_alter_post_image_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
    ]
