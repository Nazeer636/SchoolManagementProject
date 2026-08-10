from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from apps.academics.models import Mark

class InsertMarks(CreateView):
    model=Mark
    fields=('student','academic_year','class_name','subject','exam_type','marks_obtained','total_marks')

class DisplayMarks(ListView):
    model=Mark

class MarkDetails(DetailView):
    model=Mark

class UpdateMarks(UpdateView):
    model=Mark
    fields=['class_name','subject','marks_obtained']
    success_url='/academics/displaymarks'

class DeleteMarks(DeleteView):
    model=Mark
    success_url='/academics/displaymarks'