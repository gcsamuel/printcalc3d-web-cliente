
from django.db import models
from django.utils import timezone
import uuid
import os

def pedido_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    return f"pedidos/{instance.protocolo}{ext}"

class Pedido(models.Model):
    PRIORIDADE_CHOICES = [
        ("normal", "Normal"),
        ("urgente", "Urgente"),
        ("muito_urgente", "Muito urgente"),
    ]

    STATUS_CHOICES = [
        ("aguardando_arquivo", "Aguardando arquivo/ideia"),
        ("orcamento", "Orçamento"),
        ("fabricacao", "Fabricação"),
        ("acabamento", "Acabamento"),
        ("pronto", "Pronto"),
        ("entregue", "Entregue"),
    ]

    protocolo = models.CharField(max_length=20, unique=True, blank=True)
    nome = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default="normal")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="aguardando_arquivo")
    arquivo = models.FileField(upload_to=pedido_upload_path, blank=True, null=True)
    observacoes_internas = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = uuid.uuid4().hex[:10].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.protocolo} - {self.nome}"
