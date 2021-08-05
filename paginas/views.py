from django.views.generic import TemplateView 

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

# class PedidoView(TemplateView):
#     template_name = 'paginas/pedido.html'

class ModeloView(TemplateView):
    template_name = 'paginas/modelo.html'