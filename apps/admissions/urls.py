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

from django.urls import path
from apps.admissions import views as admissions_views

urlpatterns = [
    path('addadmission/',admissions_views.add_admission,name='add_admission'),
    path('addacademicyear/',admissions_views.add_academic_year,name='add_academic_year'),
    path('admissionsreport/',admissions_views.admissions_report,name='admissions_report'),
    path('updatestudent/<int:sid>/', admissions_views.update_student,name='update_student'),
    path('deletestudent/<int:sid>/', admissions_views.delete_student,name='delete_student'),

]
