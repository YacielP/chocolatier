from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto
from .serializers import ProductoSerializer 

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    # Configura filtros y ordenación
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['categoria']  # Filtra por categoría
    ordering_fields = ['precio', 'nombre']  # Ordena por precio o nombre
    search_fields = ['nombre', 'descripcion']  # Busca en nombre o descripción