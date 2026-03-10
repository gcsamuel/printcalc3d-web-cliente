
from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "nome",
            "empresa",
            "telefone",
            "whatsapp",
            "email",
            "cidade",
            "descricao",
            "prioridade",
            "arquivo",
        ]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 5, "placeholder": "Descreva sua peça, ideia ou necessidade"}),
        }

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get("arquivo")
        if not arquivo:
            return arquivo
        allowed = [".stl", ".3mf", ".gcode", ".zip", ".rar", ".7z", ".obj"]
        import os
        ext = os.path.splitext(arquivo.name)[1].lower()
        if ext not in allowed:
            raise forms.ValidationError("Envie STL, 3MF, GCODE, ZIP, RAR, 7Z ou OBJ.")
        return arquivo

class AcompanharForm(forms.Form):
    protocolo = forms.CharField(max_length=20, label="Protocolo")
