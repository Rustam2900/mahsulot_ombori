from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Product, ProductMaterial, Warehouse, Material
from .serializers import ProductSerializer, MaterialSerializer, ProductMaterialSerializer, \
    WarehouseSerializer


class MaterialRequirementView(APIView):
    def post(self, request):
        product_code = request.data.get('product_code')
        quantity = request.data.get('quantity')

        try:
            product = Product.objects.get(code=product_code)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Calculate material needs
        product_materials = ProductMaterial.objects.filter(product=product)
        required_materials = []

        for pm in product_materials:
            total_quantity_needed = pm.quantity * quantity
            remaining_quantity_needed = total_quantity_needed

            warehouses = Warehouse.objects.filter(material=pm.material).order_by('id')
            for wh in warehouses:
                if remaining_quantity_needed <= 0:
                    break
                if wh.remainder > 0:
                    used_quantity = min(wh.remainder, remaining_quantity_needed)
                    remaining_quantity_needed -= used_quantity
                    required_materials.append({
                        'warehouse_id': wh.id,
                        'material_name': pm.material.name,
                        'qty': used_quantity,
                        'price': wh.price
                    })

            if remaining_quantity_needed > 0:
                required_materials.append({
                    'warehouse_id': None,
                    'material_name': pm.material.name,
                    'qty': remaining_quantity_needed,
                    'price': None
                })

        result = {
            'result': [{
                'product_name': product.name,
                'product_qty': quantity,
                'product_materials': required_materials
            }]
        }

        return Response(result, status=status.HTTP_200_OK)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MaterialListView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetailView(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ProductMaterialListView(generics.ListAPIView):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer


class ProductMaterialDetailView(generics.RetrieveAPIView):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer


class WarehouseListView(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseDetailView(generics.RetrieveAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
