from django import forms
from apps.finance.models import FeeStructure, FeePayment


class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = ['academic_year', 'classname', 'totalfee']


class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = FeePayment
        fields = ['student_fee_account','payment_date','amount','payment_mode','remarks']
        widgets={
            'payment_date':forms.DateInput(attrs={'type':'date','class':'form-control bg-secondary text-white'}),
            'student_fee_account':forms.Select(attrs={'class':'form-control bg-secondary text-white'}),
            'amount':forms.TextInput(attrs={'class':'form-control bg-secondary text-white'}),
            'payment_mode':forms.Select(attrs={'class':'form-control bg-secondary text-white'}),
            'remarks':forms.TextInput(attrs={'class':'form-control bg-secondary text-white'})
        }