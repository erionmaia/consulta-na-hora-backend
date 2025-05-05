from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_time', 'status', 'created_at')
    list_filter = ('status', 'date_time', 'doctor')
    search_fields = ('patient__username', 'doctor__username', 'reason')
    ordering = ('-date_time',)
    
    fieldsets = (
        ('Consultation Info', {
            'fields': ('patient', 'doctor', 'date_time', 'status')
        }),
        ('Details', {
            'fields': ('reason', 'notes')
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
