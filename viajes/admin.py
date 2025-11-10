from django.contrib import admin
from .models import Viaje


@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('bus', 'conductor', 'lugar_origen', 'lugar_destino', 'fecha_salida', 'estado')
    list_filter = ('estado', 'fecha_salida')
    search_fields = ('bus__placa', 'conductor__apellido', 'lugar_origen__nombre', 'lugar_destino__nombre')
    fieldsets = (
        ('Información del Viaje', {
            'fields': ('bus', 'conductor')
        }),
        ('Ruta', {
            'fields': ('lugar_origen', 'lugar_destino', 'distancia_km')
        }),
        ('Fechas', {
            'fields': ('fecha_salida', 'fecha_llegada_estimada', 'fecha_llegada_real')
        }),
        ('Operación', {
            'fields': ('estado', 'pasajeros_confirmados', 'observaciones')
        }),
    )
    readonly_fields = ('creado_en', 'actualizado_en')
