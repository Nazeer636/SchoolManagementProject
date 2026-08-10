from django.db import models
from django.urls import reverse
from apps.admissions.models import Student,AcademicYear

class Mark(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    academic_year=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    class_name=models.CharField(max_length=10)
    subject=models.CharField(max_length=100)
    exam_type=models.CharField(max_length=10)
    marks_obtained=models.IntegerField()
    total_marks=models.IntegerField()
    exam_date=models.DateField(null=True)

    def get_absolute_url(self):
        return reverse('homepage',kwargs={'pk':self.pk})

    def __str__(self):
        return f"{self.student.name} - {self.subject} - {self.marks_obtained}"
