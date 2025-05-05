from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

class Consultation(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = 'SC', _('Agendada')
        CONFIRMED = 'CF', _('Confirmada')
        CANCELLED = 'CA', _('Cancelada')
        COMPLETED = 'CO', _('Concluída')

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='patient_consultations',
        limit_choices_to={'user_type': User.UserType.PATIENT},
        verbose_name=_('Paciente')
    )
    
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='doctor_consultations',
        limit_choices_to={'user_type': User.UserType.DOCTOR},
        verbose_name=_('Médico')
    )
    
    date_time = models.DateTimeField(
        verbose_name=_('Data e Hora')
    )
    
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.SCHEDULED,
        verbose_name=_('Status')
    )
    
    reason = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Motivo da Consulta')
    )
    
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Observações')
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Data de Criação')
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Data de Atualização')
    )

    class Meta:
        verbose_name = _('Consulta')
        verbose_name_plural = _('Consultas')
        ordering = ['date_time']

    def __str__(self):
        return f"{self.patient.get_full_name()} - {self.doctor.get_full_name()} - {self.date_time.strftime('%d/%m/%Y %H:%M')}"

    def can_be_cancelled(self):
        return self.status in [self.Status.SCHEDULED, self.Status.CONFIRMED]

    def can_be_confirmed(self):
        return self.status == self.Status.SCHEDULED
