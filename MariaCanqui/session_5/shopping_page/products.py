import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class products:
    def __init__(self):
        self.products = {}

    def add_products(self, code, name, price, amount):
        logger.info('Adding products')

        data = {}
        data['name'] = name
        data['price'] = price
        data['amount'] = amount
        self.products[code] = data

    def get_all_products(self):
        return self.products

    def get_all_prices(self):
        print(self.products)
        for i in self.products:
            print("Code:",i, "Name:", self.products[i]["name"], "Price:", self.products[i]["price"])

    def get_all_amounts(self):
        for i in self.products:
            print("Code:",i, "Name:", self.products[i]["name"], "Amount:", self.products[i]["amount"] )

    def update_amount_aftersold(self, code, amount):
        self.products[code] = self.products[code]["amount"] - amount

    def update_amount(self, code, amount):
        self.products[code]["amount"] = amount

