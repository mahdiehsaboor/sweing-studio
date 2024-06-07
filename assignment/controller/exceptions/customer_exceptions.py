class CustomerNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Customer not found")