from django import forms

from resume_uploads.models import Resume

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'resume_file': forms.FileInput(attrs={'class': 'form-control border border-dark'}),
        }