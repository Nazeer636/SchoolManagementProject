from django.contrib import admin
from apps.admissions.models import Student,AcademicYear

class StudentAdmin(admin.ModelAdmin):
    list_display=['admission_number','name','class_name']

class AcademicYearAdmin(admin.ModelAdmin):
    list_display=['year_name','is_active']

admin.site.register(Student,StudentAdmin)
admin.site.register(AcademicYear,AcademicYearAdmin)
