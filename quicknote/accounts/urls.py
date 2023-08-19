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
    path('login/', views.accounts_login, name="login"),
    path('logout/', views.accounts_logout, name="logout"),
    path('password_change/', views.accounts_password_change, name="password_change"),
    path('password_reset/', views.accounts_password_reset, name="password_reset"),
    path('signup/', views.accounts_signup, name="signup"),
    path('delete/', views.accounts_delete, name="delete"),
    path('profile/', views.accounts_profile, name="profile"),

]
