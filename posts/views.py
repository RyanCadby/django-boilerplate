from django.shortcuts import render


def articleArchive(request):
    return render(request, 'article-archive.html')