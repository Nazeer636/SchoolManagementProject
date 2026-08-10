from django.urls import path
from apps.academics import views as academic_views 
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('insertmarks/',login_required(academic_views.InsertMarks.as_view()),name='insert_marks'),
    path('displaymarks/',login_required(academic_views.DisplayMarks.as_view()),name='display_marks'),
    path('markdetails/<int:pk>',login_required(academic_views.MarkDetails.as_view()),name='mark_details'),
    path('updatemarks/<int:pk>',login_required(academic_views.UpdateMarks.as_view()),name='update_marks'),
    path('deletemarks/<int:pk>',login_required(academic_views.DeleteMarks.as_view()),name='delete_marks'),
]