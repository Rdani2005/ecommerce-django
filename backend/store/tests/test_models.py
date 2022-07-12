"""
    ================================================================================================================================
    Copyright (C) 2022 by Daniel Ricardo Sequeira Campos

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
    files (the "Software"), to deal in the Software without restriction, including without l> imitation the rights to use, copy, 
    modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software 
    is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
    IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    =================================================================================================================================
"""
# ---------------------- Libraries and modules --------------------
# Django: http://docs.djangoproject.com/
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
# Own modules
from store.models import Category, Product # DB Models 

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