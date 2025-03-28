from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def validate(self, attrs):
        # Crea una instancia del modelo con los datos del serializador
        producto = Producto(**attrs)

        # Llama a full_clean para validar los campos definidos en el modelo
        producto.full_clean()  # Esto ejecuta el método clean() del modelo
        return attrs
