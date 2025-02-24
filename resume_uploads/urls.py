from django.urls import path

from resume_uploads import views

urlpatterns = [
    path('', views.uploads, name='upload_resume'),
]