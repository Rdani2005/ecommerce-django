from decimal import Decimal
from store.models import Product
class Basket():
    """
        Class with basket behaviors
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {}

        self.basket = basket

    def add(self, product):
        """Add a product"""
        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price)}

        self.save()

    def __iter__(self):
        products_ids = self.basket.keys()
        products = Product.products.filter(id__in = products_ids)
        basket = self.basket.copy()

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())


    def update(self, product, qty):
        product_id = str(product)
        
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty

        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            print(product_id)
            self.save()

    def save(self):
        self.session.modified = True