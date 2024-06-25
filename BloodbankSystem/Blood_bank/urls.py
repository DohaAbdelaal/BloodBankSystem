"""
URL configuration for Blood_bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from donation import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name='Home'),
    path('donor/', views.Donor_info,name='donor'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('blood_request/', views.blood_request, name='blood_request'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.FAQ, name='FAQ'),
    
    
]
