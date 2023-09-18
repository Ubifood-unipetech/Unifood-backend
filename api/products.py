from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models import Product, ProductType
from api.permissions import IsObjRestaurantMember
    
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=ProductType.objects.all())
    type_info = ProductTypeSerializer(source='type', read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        extra_fields = ['type_mnemo', 'type_id']

class ProductTypes(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing product types.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAdminUser]

class Products(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsObjRestaurantMember]