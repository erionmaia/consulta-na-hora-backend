from django.urls import path
from .views import (
    ConsultationListView,
    ConsultationDetailView,
    ConsultationStatusUpdateView,
    DoctorAvailabilityView
)

urlpatterns = [
    path('', ConsultationListView.as_view(), name='consultation_list'),
    path('<int:pk>/', ConsultationDetailView.as_view(), name='consultation_detail'),
    path('<int:pk>/status/', ConsultationStatusUpdateView.as_view(), name='consultation_status'),
    path('doctors/<int:doctor_id>/availability/', DoctorAvailabilityView.as_view(), name='doctor_availability'),
    path('doctor/<int:doctor_id>/availability/', DoctorAvailabilityView.as_view(), name='doctor-availability'),
] 