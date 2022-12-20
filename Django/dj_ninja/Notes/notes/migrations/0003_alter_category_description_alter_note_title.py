# Generated by Django 4.1.4 on 2022-12-19 10:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=tinymce.models.HTMLField(),
        ),
    ]
