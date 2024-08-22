from rest_framework import serializers

from inventory.models import Product, Material, ProductMaterial, Warehouse


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'code')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('name',)


class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = ('product', 'material', 'quantity')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('material', 'remainder', 'price')


class ProductRequestSerializer(serializers.Serializer):
    product_code = serializers.IntegerField()
    quantity = serializers.FloatField()
