from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'report/home.html'
    context_object_name = 'reports'
    paginate_by = 3

class ReportDetailView(DetailView):
    model = Report





def home(request):
    context = {
        'reports': Report.objects.all()
    }
    return render(request, 'report/home.html', context)
# Create your views here.
