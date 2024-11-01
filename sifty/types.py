from sys import getsizeof

class Instance:
    def __init__(self, object: object = None):
        self.object = object
    
    def __str__(self):
        return str(self.object)
    
    def __sizeof__(self):
        return getsizeof(self.object)
    
    @property
    def typeof(self):
        return type(self.object).__name__