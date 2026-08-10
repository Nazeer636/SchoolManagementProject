from django import forms
from apps.admissions.models import Student,AcademicYear

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=[
                'admission_number',
                'name','father_name','mother_name',
                'gender','class_name',
                'date_of_birth','contact',
                'address'
                ]
        widgets={
            'date_of_birth':forms.DateInput(attrs={'type':'date'}),
            'gender':forms.RadioSelect,
            'admission_number':forms.TextInput(attrs={'class':'form-control bg-secondary text-white'}),
            'name':forms.TextInput(attrs={'class':'form-control bg-secondary text-white'}),
            'father_name':forms.TextInput(attrs={'class':'form-control bg-secondary text-white'}),
            'mother_name':forms.TextInput(attrs={'class':'form-control bg-secondary text-white'}),
            'contact':forms.TextInput(attrs={'class':'form-control bg-secondary text-white'}),
            'address':forms.Textarea
        }

class AcademicYearModelForm(forms.ModelForm):
    class Meta:
        model=AcademicYear
        fields=['year_name','is_active']