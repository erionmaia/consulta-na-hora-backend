from rest_framework import serializers
from .models import Consultation
from users.serializers import UserProfileSerializer
from users.models import User
from django.utils import timezone

class ConsultationSerializer(serializers.ModelSerializer):
    patient = UserProfileSerializer(read_only=True)
    doctor = UserProfileSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(user_type=User.UserType.PATIENT),
        source='patient',
        write_only=True
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(user_type=User.UserType.DOCTOR),
        source='doctor',
        write_only=True
    )

    class Meta:
        model = Consultation
        fields = ('id', 'patient', 'doctor', 'patient_id', 'doctor_id',
                  'date_time', 'status', 'reason', 'notes',
                  'created_at', 'updated_at')
        read_only_fields = ('status', 'created_at', 'updated_at')

    def validate(self, attrs):
        date_time = attrs.get('date_time')
        
        # Check if the date is in the future
        if date_time and date_time < timezone.now():
            raise serializers.ValidationError(
                {"date_time": "A data da consulta deve ser futura."}
            )
        
        # Check if the doctor is available at that time
        if date_time and attrs.get('doctor'):
            existing_consultation = Consultation.objects.filter(
                doctor=attrs['doctor'],
                date_time=date_time,
                status__in=[Consultation.Status.SCHEDULED, Consultation.Status.CONFIRMED]
            ).exists()
            
            if existing_consultation:
                raise serializers.ValidationError(
                    {"date_time": "O médico já possui uma consulta agendada neste horário."}
                )
        
        return attrs

class ConsultationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ('id', 'status')
        read_only_fields = ('id',)

    def validate_status(self, value):
        consultation = self.instance
        
        if value == Consultation.Status.CANCELLED and not consultation.can_be_cancelled():
            raise serializers.ValidationError(
                "Esta consulta não pode ser cancelada no momento."
            )
        
        if value == Consultation.Status.CONFIRMED and not consultation.can_be_confirmed():
            raise serializers.ValidationError(
                "Esta consulta não pode ser confirmada no momento."
            )
        
        return value 