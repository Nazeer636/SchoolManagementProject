from django.urls import path
from apps.finance import views as finance_views

urlpatterns = [
    path('setfeestructure/',finance_views.set_fee_structure,name='set_fee_structure'),
    path('collectfee/',finance_views.collect_fee,name='collect_fee'),
    path('feereceipt/<int:rcptno>/',finance_views.show_fee_receipt,name='show_fee_receipt'),
    path('feeduesreport/',finance_views.fee_dues_report,name='fee_dues_report'),
    path('feecollectionreport/',finance_views.fee_collection_report,name='fee_collection_report')
    ]

