from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404


def home(request):
    return render(request, 'resume_site/home.html')

def about(request):
    return render(request, 'resume_site/about.html')

def resume(request):
    try:
        return FileResponse(open('static/document/Resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()