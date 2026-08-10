from django.shortcuts import render,redirect
from apps.office.models import CerificateRequest
from apps.office.forms import CertificateRequestForm
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def certificate_request_list(request):
    requests=CerificateRequest.objects.all()
    return render(request,'office/certificate-request-list.html',{'requests':requests})


@login_required
def create_certificate_request(request):
    form=CertificateRequestForm()
    myform={'form':form}

    if request.method=='POST':
        form=CertificateRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_request_list')
    return render(request,'office/create-certificate-request.html',myform)

@login_required
def update_certificate_request(request,cid):
    req=CerificateRequest.objects.get(id=cid)
    form=CertificateRequestForm(instance=req)
    
    if request.method=='POST':
        sform=CertificateRequestForm(request.POST,instance=req)
        if sform.is_valid():
            sform.save()
        return redirect('certificate_request_list')
    
    return render(request,'office/create-certificate-request.html',{'form':form})
            

@login_required
def delete_certificate_request(request,cid):
    request=CerificateRequest.objects.get(id=cid)
    request.delete()
    return redirect('certificate_request_list')

class FirstView(View):
    def get(self,request):
        return HttpResponse('This is get')
    def post(self,request):
        return HttpResponse('This is post')

