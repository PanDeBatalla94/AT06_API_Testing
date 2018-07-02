import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class purchaseItem():
    def __init__(self):
        sold = {}

    def add_item(self, code, amount):
        logger.info('puchasing ...')
        data = {}
        data["code"] = code
        data["amount"] = amount
        self.sold[len(self.sold)+1] = data


    def get_all_sold(self):
        return self.sold

