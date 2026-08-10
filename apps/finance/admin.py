from django.contrib import admin
from apps.finance.models import FeeStructure,StudentFeeAccount,FeePayment

class FeeStructureAdmin(admin.ModelAdmin):
    list_display=['academic_year','classname','totalfee']

class StudentFeeAccountAdmin(admin.ModelAdmin):
    list_display=['student','totalfee','feepaid','feedue']

class FeepaymentAdmin(admin.ModelAdmin):
    list_display=['student_fee_account','amount','payment_date']

admin.site.register(FeeStructure,FeeStructureAdmin)
admin.site.register(StudentFeeAccount,StudentFeeAccountAdmin)
admin.site.register(FeePayment,FeepaymentAdmin)
