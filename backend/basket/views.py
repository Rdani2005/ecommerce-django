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
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .basket import Basket
from store.models import Product

def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)

    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)

        response = JsonResponse({
            'test': 'data'
        })

        return response