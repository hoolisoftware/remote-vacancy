from django.shortcuts import render

def page_404(request, exception=Exception):
    return render(request, 'core/404.django-html', status=404)