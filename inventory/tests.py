from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, Material, ProductMaterial, Warehouse

from rest_framework.test import APIClient


class ProductMaterialAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Product1', code='P001')
        self.material = Material.objects.create(name='Material1')
        self.product_material = ProductMaterial.objects.create(product=self.product, material=self.material, quantity=2)
        self.warehouse = Warehouse.objects.create(material=self.material, remainder=100, price=10.0)
        self.url = '/product-material/'  # URL endpointi

    def test_post_product_material_api(self):
        data = {
            'product_code': 'P001',
            'quantity': 5
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('product_name', response.data)
        self.assertIn('product_materials', response.data)

    def test_post_product_material_api_product_not_found(self):
        data = {
            'product_code': 'P999',
            'quantity': 5
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'error': 'Product not found'})


class ProductViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Product1', code='P001')
        self.url_list = '/products/'
        self.url_detail = f'/products/{self.product.id}/'

    def test_get_product_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_get_product_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Product1')


class MaterialViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.material = Material.objects.create(name='Material1')
        self.url_list = '/materials/'
        self.url_detail = f'/materials/{self.material.id}/'

    def test_get_material_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_get_material_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Material1')


class ProductMaterialViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.material = Material.objects.create(name='Material1')
        self.product = Product.objects.create(name='Product1', code='P001')
        self.product_material = ProductMaterial.objects.create(product=self.product, material=self.material, quantity=2)
        self.url_list = '/product-materials/'
        self.url_detail = f'/product-materials/{self.product_material.id}/'

    def test_get_product_material_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_get_product_material_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product'], self.product.id)
        self.assertEqual(response.data['material'], self.material.id)


class WarehouseViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.material = Material.objects.create(name='Material1')
        self.warehouse = Warehouse.objects.create(material=self.material, remainder=100, price=10.0)
        self.url_list = '/warehouses/'
        self.url_detail = f'/warehouses/{self.warehouse.id}/'

    def test_get_warehouse_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_get_warehouse_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['material'], self.material.id)
