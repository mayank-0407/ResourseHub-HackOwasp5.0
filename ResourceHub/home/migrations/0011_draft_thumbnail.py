# Generated by Django 4.2 on 2023-05-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_draft_description_alter_draft_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='thumbnail',
            field=models.FileField(blank=True, upload_to='media/Drafts'),
        ),
    ]
