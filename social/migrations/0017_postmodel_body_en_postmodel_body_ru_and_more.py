# Generated by Django 4.0 on 2022-01-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_alter_postmodel_created_at_alter_postmodel_dislike_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='body_en',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='body'),
        ),
    ]
