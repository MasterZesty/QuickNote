"""
URL configuration for quicknote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name="list_note"),
    path('create/', views.create_note, name="create_note"),
    path('delete/<str:note_id>/', views.delete_note, name="delete_note"),
    path('edit/<str:note_id>/', views.edit_note, name="edit_note"),
]
