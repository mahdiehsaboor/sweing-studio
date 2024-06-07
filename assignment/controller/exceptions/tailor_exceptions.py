class TailorNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Tailor not found")