class PixError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return super().__str__()
