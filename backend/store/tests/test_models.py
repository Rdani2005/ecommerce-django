
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from store.models import Category, Product

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def  test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))


    def test_category_url(self):
        data = self.data1
        response = self.client.post(
            reverse('store:category_list', args=[data.slug])
        )
        self.assertEqual(response.status_code, 200)



class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')


        self.data1 = Product.objects.create(
            category_id=1,
            title='product',
            created_by_id=1,
            slug='product',
            price='20.00',
            image='django'
        )

        self.data2 = Product.objects.create(
            category_id=1,
            title='product-2',
            created_by_id=1,
            slug='product-2',
            price='50.00',
            image='django'
        )

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'product')

    def test_products_url(self):
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        self.assertEqual(url, '/product/product/')
        response = self.client.post(
            reverse('store:product_detail', args=[data.slug])
        )
        self.assertEqual(response.status_code, 200)


    def test_products_custom_manager_basic(self):
        data = Product.objects.all()
        self.assertEqual(data.count(), 2)