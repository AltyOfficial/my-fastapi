class HelloException(Exception):
    
    def __init__(self, title: str) -> None:
        self.title = title