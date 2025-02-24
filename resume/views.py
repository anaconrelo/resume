from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache

@never_cache
def resume(request):

    return render(request, 'main.html')