
from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("protocolo", "nome", "prioridade", "status", "created_at")
    list_filter = ("prioridade", "status", "created_at")
    search_fields = ("protocolo", "nome", "email", "whatsapp")
