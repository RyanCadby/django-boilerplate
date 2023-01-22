from django.urls import path
from . import views

urlpatterns = [
    path('', views.articleArchive, name='article archive'),
]