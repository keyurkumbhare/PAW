from django.contrib import admin
from django.urls import path
from . import views
from .views import ReportListView, ReportDetailView

urlpatterns = [
    path('', ReportListView.as_view(), name='home-page'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
]
