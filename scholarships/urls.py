from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarshipArchive, name='scholarship archive'),
]