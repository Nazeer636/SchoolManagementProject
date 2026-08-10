from django import forms
from .models import CerificateRequest

class CertificateRequestForm(forms.ModelForm):
    class Meta:
        model=CerificateRequest
        fields=['student','type','reason','request_date','status','issued_date']
        widgets={
            'request_date':forms.DateInput(attrs={'type':'date'}),
            'issued_date':forms.DateInput(attrs={'type':'date'})
        }