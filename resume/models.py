import os
from django.db import models

class Resume(models.Model):
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)
    
    class Meta:
        db_table = 'resume'