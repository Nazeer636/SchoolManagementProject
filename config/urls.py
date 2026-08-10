"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from apps.admissions import views as admissions_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admissions_views.homepage,name='homepage'),
    path('logout', admissions_views.logout,name='logout'),
    path('admissions/',include('apps.admissions.urls')),
    path('finance/',include('apps.finance.urls')),
    path('office/',include('apps.office.urls')),
    path('academics/',include('apps.academics.urls')),
    path('accounts/',include('django.contrib.auth.urls'))
]
