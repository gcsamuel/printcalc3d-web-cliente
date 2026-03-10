
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PedidoForm, AcompanharForm
from .models import Pedido

def home(request):
    if request.method == "POST":
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save()
            return redirect("sucesso", protocolo=pedido.protocolo)
    else:
        form = PedidoForm()
    return render(request, "pedidos/home.html", {"form": form})

def sucesso(request, protocolo):
    pedido = get_object_or_404(Pedido, protocolo=protocolo)
    return render(request, "pedidos/sucesso.html", {"pedido": pedido})

def acompanhar(request):
    form = AcompanharForm(request.GET or None)
    pedido = None
    if form.is_valid():
        protocolo = form.cleaned_data["protocolo"].strip().upper()
        pedido = Pedido.objects.filter(protocolo=protocolo).first()
        if not pedido:
            messages.error(request, "Protocolo não encontrado.")
    return render(request, "pedidos/acompanhar.html", {"form": form, "pedido": pedido})
