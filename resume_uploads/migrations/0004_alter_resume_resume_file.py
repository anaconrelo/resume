# Generated by Django 4.2 on 2025-02-24 08:38

from django.db import migrations, models
import resume_uploads.models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_uploads', '0003_alter_resume_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume_file',
            field=models.FileField(max_length=900, upload_to='resumes/%Y/%m/', validators=[resume_uploads.models.validate_extension]),
        ),
    ]
