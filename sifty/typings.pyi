#from typing import overload

class Instance:
    def __init__(self, obj: object): ...
    def __str__(self) -> str: ...
    def __sizeof__(self) -> int: ...

    @property
    def typeof(self) -> str: ...
