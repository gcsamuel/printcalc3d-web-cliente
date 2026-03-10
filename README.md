# PrintCalc3D Web Cliente

Portal web em Django para o cliente:
- abrir pedido
- enviar arquivo
- acompanhar status pelo protocolo

## Recursos
- formulário de pedido
- upload de STL / 3MF / GCODE / ZIP
- prioridade: normal, urgente, muito urgente
- protocolo automático
- página pública para acompanhar pedido
- admin Django

## Rodar
```bash
cd printcalc3d_web_cliente
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URLs
- formulário: `/`
- acompanhar pedido: `/acompanhar/`
- admin: `/admin/`

## Próxima fase
- integrar com o app interno
- API para sincronizar pedidos
- autenticação de clientes
- notificações automáticas
