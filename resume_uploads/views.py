from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from resume_uploads.models import Resume
from resume_uploads.forms import UploadFileForm
# Create your views here.
@never_cache
def uploads(request):
    resumeForm = UploadFileForm()
    errors = None
    if request.method == 'POST':
        try:
            resumeForm = UploadFileForm(request.POST, request.FILES)
            if resumeForm.is_valid():
                resume = resumeForm.save(commit=False)
                Resume.objects.update_or_create(id=1, defaults={'resume_file': resume.resume_file})

                return redirect('resume')
            else:
                errors = resumeForm.errors
        except Exception as e:
            print(e)
            errors = e

    context = {
        'form': resumeForm,
        'error': errors,
    }
    return render(request, 'uploads.html', context)