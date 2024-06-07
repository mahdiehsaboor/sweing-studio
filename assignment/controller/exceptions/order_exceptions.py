class OrderNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Order not found")