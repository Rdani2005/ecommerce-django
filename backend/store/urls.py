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
# ------------------------- Libraries and Modules ------------------------------
# Django: http://docs.djangoproject.com/
from django.urls import path
# Own Modules
from . import views # Importing the functions views

# Name of the application
app_name = 'store'

""" 
---------------------------------------------
Setting up the Urls of the Django application
---------------------------------------------
1. Home View | This is the main view of the entire website
2. Product View | This is the Detail view of an specific product
3. Category View | This is the list of products avialable in the specific category
"""
urlpatterns = [
    path('', views.products_all.as_view(), name='products_all'), # Home view
    path('<slug:slug>', views.product_detail.as_view(), name='product_detail'), # Product detail view
    path('category/<slug:category_slug>/', views.category_list.as_view(), name='category_list') # Category list view
]
