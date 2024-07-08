#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="Good") -> None:
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, condition):
        if isinstance(condition, str):
            self._condition = condition
        else:
            print("condition must be a string")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
