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

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', views.login, name="login"),
    path('accounts/logout/', views.logout, name="logout"),
    path('accounts/password_change/', views.password_change, name="password_change"),
    path('accounts/password_reset/', views.password_reset, name="password_reset"),
    path('accounts/signup/', views.signup, name="signup"),
    path('accounts/delete/', views.delete, name="delete"),
]
