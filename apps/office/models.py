from django.db import models
from apps.admissions.models import Student

class CerificateRequest(models.Model):
    certificate_choices=[
        ('TC','Transfer Certificate'),
        ('Study','Study Certificate')
    ]
    status_choices=[
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
        ('Issued','Issued')
    ]
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    type=models.CharField(max_length=30,choices=certificate_choices)
    reason=models.TextField()
    request_date=models.DateField(null=True)
    status=models.CharField(max_length=30,choices=status_choices)
    issued_date=models.DateField(null=True)

    def __str__(self):
        return f'{self.student.name} - {self.type}'

