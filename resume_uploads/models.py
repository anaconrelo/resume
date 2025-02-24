import os
from django.db import models
from django.forms import ValidationError

def validate_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Hanya fail PDF sahaja.')
    
resumes = 'resumes/%Y/%m/'

class Resume(models.Model):
    resume_file = models.FileField(upload_to=resumes, validators=[validate_extension], max_length=900)
    
    class Meta:
        db_table = 'resume'
