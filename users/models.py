from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class UserType(models.TextChoices):
        PATIENT = 'PA', _('Paciente')
        DOCTOR = 'DO', _('Médico')

    user_type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.PATIENT,
        verbose_name=_('Tipo de Usuário')
    )
    
    # Additional fields for doctors
    crm = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_('CRM')
    )
    specialty = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Especialidade')
    )
    
    # Additional fields for patients
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Data de Nascimento')
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_('Telefone')
    )

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_user_type_display()})"

    @property
    def is_doctor(self):
        return self.user_type == self.UserType.DOCTOR

    @property
    def is_patient(self):
        return self.user_type == self.UserType.PATIENT
