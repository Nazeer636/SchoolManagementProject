from django.urls import path
from apps.office import views as office_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('certificaterequestlist/',office_views.certificate_request_list,name='certificate_request_list'),
    path('createcertificaterequest/',office_views.create_certificate_request,name='create_certificate_request'),
    path('updatecertificaterequest/<int:cid>/',office_views.update_certificate_request,name='update_certificate_request'),
    path('deletecertificaterequest/<int:cid>/',office_views.delete_certificate_request,name='delete_certificate_request'),
    path('firstview/',login_required(office_views.FirstView.as_view()),name='first_view')
    ]

