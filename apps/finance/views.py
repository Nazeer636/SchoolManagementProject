import urllib.request
from django.shortcuts import render,redirect
from apps.finance.forms import FeeStructureForm,FeePaymentForm
from apps.admissions.views import homepage
from django.db import transaction
from apps.finance.models import StudentFeeAccount,FeePayment
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.utils import ImageReader
from io import BytesIO
from django.contrib.auth.decorators import login_required


@login_required
def show_fee_receipt(request,rcptno):
    receipt=FeePayment.objects.get(id=rcptno)
    studentname=receipt.student_fee_account.student.name
    classname=receipt.student_fee_account.student.class_name
    amount=receipt.amount
    payment_date=receipt.payment_date
    payment_mode=receipt.payment_mode

    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline'
    pdffile=canvas.Canvas(response)

    url='https://teluguwebguru.in/assets/img/logo/logo-black.png'
    image=BytesIO(urllib.request.urlopen(url).read())
    logo=ImageReader(image)
    pdffile.drawImage(logo, 220, 770, width=120, height=50)
    pdffile.drawString(250,750," LS FEE RECEIPT")
    pdffile.drawString(150,700,f"Receipt No :{rcptno}")
    pdffile.drawString(150,670,f"Student Name :{studentname}")
    pdffile.drawString(150,640,f"Class :{classname}")
    pdffile.drawString(150,610,f"Amount :{amount}")
    pdffile.drawString(150,580,f"Date :{payment_date}")
    pdffile.drawString(150,550,f"Mode :{payment_mode}")
    pdffile.drawString(450,450,"Signature")


    pdffile.showPage()
    pdffile.save()
    return response

@login_required 
def set_fee_structure(request):
    form=FeeStructureForm()
    myform={'form':form}

    if request.method=='POST':
        form=FeeStructureForm(request.POST)
        if form.is_valid():
          if form.is_valid():
            form.save()
            return homepage(request)
    return render(request,'finance/set-fee-Structure.html',myform)

@login_required
def collect_fee(request):
    form=FeePaymentForm()
    myform={'form':form}

    if request.method=='POST':
        form=FeePaymentForm(request.POST)
        receiptid=0
        if form.is_valid():
            with transaction.atomic():
                feepayment=form.save()
                receiptid=feepayment.id
                feeaccount=feepayment.student_fee_account
                feeaccount.feepaid=feeaccount.feepaid+feepayment.amount
                feeaccount.feedue=feeaccount.feedue-feepayment.amount
                feeaccount.save()
                values={'feeaccount':feepayment.student_fee_account,'feepayment':feepayment}
            return redirect('show_fee_receipt',rcptno=receiptid)

    return render(request,'finance/collect-fee.html',myform)

@login_required
def fee_dues_report(request):
    feeaccounts=StudentFeeAccount.objects.all()
    print(feeaccounts)
    values={'feeaccounts':feeaccounts}
    return render(request,'finance/fee-dues-report.html',values)

@login_required
def fee_collection_report(request):
    feepayments=FeePayment.objects.all()
    values={'feepayments':feepayments}
    return render(request,'finance/fee-collection-report.html',values)
    

