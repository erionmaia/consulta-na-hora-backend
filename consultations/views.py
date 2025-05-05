from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Consultation
from .serializers import ConsultationSerializer, ConsultationStatusSerializer
from users.models import User

# Create your views here.

class ConsultationListView(generics.ListCreateAPIView):
    serializer_class = ConsultationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_doctor:
            return Consultation.objects.filter(doctor=user)
        return Consultation.objects.filter(patient=user)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class ConsultationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConsultationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_doctor:
            return Consultation.objects.filter(doctor=user)
        return Consultation.objects.filter(patient=user)

class ConsultationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ConsultationStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_doctor:
            return Consultation.objects.filter(doctor=user)
        return Consultation.objects.filter(patient=user)

    def update(self, request, *args, **kwargs):
        consultation = self.get_object()
        serializer = self.get_serializer(consultation, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorAvailabilityView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        date = self.request.query_params.get('date')
        
        if not date:
            return Consultation.objects.none()
        
        try:
            date = timezone.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return Consultation.objects.none()
        
        # Get all consultations for the doctor on the specified date
        return Consultation.objects.filter(
            doctor_id=doctor_id,
            date_time__date=date,
            status__in=[Consultation.Status.SCHEDULED, Consultation.Status.CONFIRMED]
        )
