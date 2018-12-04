from django.shortcuts import render
from .models import NewUrl, DeleteUrl


def displayNewDelete(request):
    new_urls = NewUrl.objects.all()
    delete_urls = DeleteUrl.objects.all()

    return render(request, 'sitemaptrack/url_list.html', {'new_urls': new_urls, 'delete_urls': delete_urls})
