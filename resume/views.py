from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache

from resume_uploads.models import Resume

#from resume.forms import UploadFileForm


@never_cache
def resume(request):
    resume = Resume.objects.get(id=1)
    context = {
        'resume': resume
    }
    return render(request, 'main.html', context)
