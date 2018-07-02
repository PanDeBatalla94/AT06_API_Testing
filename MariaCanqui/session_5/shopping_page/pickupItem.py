import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class pickupItem():
    def __init__(self):
        pick = {}

    def add_item(self, code, amount):
        logger.info('adding items')
        self.pick[code] = amount

    def get_pick(self):
        return self.pick