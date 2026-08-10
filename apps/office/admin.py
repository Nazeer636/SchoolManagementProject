from django.contrib import admin
from apps.office.models import CerificateRequest

class CertificateRequestAdmin(admin.ModelAdmin):
    list_display=['student','type','request_date','status']

admin.site.register(CerificateRequest,CertificateRequestAdmin)
