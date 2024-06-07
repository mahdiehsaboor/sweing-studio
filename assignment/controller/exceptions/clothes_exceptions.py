class ClothesNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Clothes not found")