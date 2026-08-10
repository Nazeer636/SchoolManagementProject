from django.contrib import admin
from apps.academics.models import Mark

class MarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks_obtained']

admin.site.register(Mark,MarkAdmin)
