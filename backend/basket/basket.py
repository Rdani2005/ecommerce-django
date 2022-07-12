class Basket():
    """
        Class with basket behaviors
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {
                'number': 1212132334455
            }

        self.basket = basket
