from django.db import models
from apps.admissions.models import AcademicYear,Student

class FeeStructure(models.Model):
    academic_year=models.ForeignKey(
        AcademicYear,on_delete=models.CASCADE )
    classname=models.IntegerField()
    totalfee=models.DecimalField(max_digits=10,decimal_places=4)
    class Meta:
            constraints=[
                models.UniqueConstraint(
                    fields=['academic_year','classname'],
                    name='unique_feestructure_academicyear_classname'
                )
            ]

class StudentFeeAccount(models.Model):
    student=models.ForeignKey(
        Student,on_delete=models.CASCADE)
    academic_year=models.ForeignKey(
         AcademicYear,on_delete=models.CASCADE  )
    totalfee=models.DecimalField(max_digits=10,decimal_places=4)
    feepaid=models.DecimalField(max_digits=10,decimal_places=4)
    feedue=models.DecimalField(max_digits=10,decimal_places=4)
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['student','academic_year'],
                name='unique_feeaccount_student_academic_year'
            )
        ]
        
    def __str__(self):
         return f"{self.student.admission_number} - {self.student.name}"

class FeePayment(models.Model):
    payment_choices=[('UPI','UPI'),('CASH','CASH'),('CARD','CARD'),('BANK','BANK')]
    student_fee_account=models.ForeignKey(StudentFeeAccount,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=4)
    payment_date=models.DateField()
    payment_mode=models.CharField(max_length=10,choices=payment_choices)
    remarks=models.CharField(max_length=1000)


