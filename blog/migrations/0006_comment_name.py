# Generated by Django 5.0.6 on 2024-06-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_comment_comment_post_alter_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
