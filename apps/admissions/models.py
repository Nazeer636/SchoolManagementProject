from django.db import models

class Student(models.Model):
    GenderChoices=[
        ('Male','Male'),
        ('Female','Female')
    ]
    ClassChoices=[
            ('LKG','LKG'),
            ('UKG','UKG'),
            ('1','Class 1'),
            ('2','Class 2'),
            ('3','Class 3'),
            ('4','Class 4'),
            ('5','Class 5'),
            ('6', 'Class 6'),
            ('7', 'Class 7'),
            ('8', 'Class 8')
        ]
    admission_number=models.CharField(max_length=10,unique=True,null=True)
    name=models.CharField(max_length=100,null=True)
    father_name=models.CharField(max_length=100,null=True)
    mother_name=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=10,choices=GenderChoices,null=True)
    class_name=models.CharField(max_length=10,choices=ClassChoices,null=True)
    date_of_birth=models.DateField(null=True)
    contact=models.CharField(max_length=15)
    address=models.CharField(max_length=1000,null=True)
    admission_date=models.DateField(auto_now_add=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.admission_number}'

class AcademicYear(models.Model):
    year_name=models.CharField(max_length=10)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year_name}"

   
     
