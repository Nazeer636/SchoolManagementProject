from django.shortcuts import render
from apps.admissions.forms import StudentModelForm,AcademicYearModelForm
from apps.admissions.models import AcademicYear,Student
from apps.finance.models import FeeStructure,StudentFeeAccount,FeePayment
from django.db import transaction
from django.db.models import Sum
from django.contrib.auth.decorators import login_required,permission_required

@login_required
def homepage(request):
    totalstudents=Student.objects.count()
    feecollected=FeePayment.objects.aggregate(Sum('amount'))['amount__sum']
    feeduetotal=StudentFeeAccount.objects.aggregate(Sum('feedue'))['feedue__sum']
    username=request.user
    values={'totalstudents':totalstudents,'feecollected':feecollected,'feeduetotal':feeduetotal,'username':username}
    response=render(request,'home.html',values)
    response.set_cookie("username",username)
    response.set_cookie("totalstudents",totalstudents)
    return response

def logout(request):
    return render(request,'registration/logout.html')

@login_required
def add_academic_year(request):
    form=AcademicYearModelForm()
    myform={'form':form}

    if request.method=='POST':
        form=AcademicYearModelForm(request.POST)
        form.save()
        return homepage(request)
    
    return render(request,'admissions/add_academic_year.html',myform)

@login_required
def add_admission(request):
    form=StudentModelForm()
    myform={'form':form}

    if request.method=='POST':
        filledform=StudentModelForm(request.POST)
        with transaction.atomic():
                if filledform.is_valid():
                    student=filledform.save()
                    current_academic_year=AcademicYear.objects.get(is_active=True)
                    feestructures=FeeStructure.objects.filter(academic_year=current_academic_year)&FeeStructure.objects.filter(classname=student.class_name)
                    totalfee=feestructures[0].totalfee
                    StudentFeeAccount.objects.create(student=student,academic_year=current_academic_year,totalfee=totalfee,feepaid=0,feedue=totalfee)
                else:
                    print(filledform.errors)
        return homepage(request)
    return render(request,'admissions/add_admission.html',myform)

@login_required
def admissions_report(request):
    students=Student.objects.all()
    username=request.COOKIES['username']
    totalstudents=request.COOKIES['totalstudents']

    values={'students':students,'username':username,'totalstudents':totalstudents}
    return render(request,'admissions/admissions_report.html',values)

@login_required
@permission_required('admissions.change_student')
def update_student(request,sid):
    s=Student.objects.get(id=sid)
    form=StudentModelForm(instance=s)

    if request.method=='POST':
        sform=StudentModelForm(request.POST,instance=s)
        if sform.is_valid():
            sform.save()
        return admissions_report(request)
        
    return render(request,'admissions/add_admission.html',{'form':form})

@login_required
@permission_required('admissions.delete_student')
def delete_student(request,sid):
    s=Student.objects.get(id=sid)
    s.delete()
    return admissions_report(request)
