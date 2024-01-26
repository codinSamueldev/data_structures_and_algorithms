""" 
This module will recreate how an array is created and its common methods.
"""

from typing import Any


class MyArray:
    def __init__(self):
        self.length: int = 0
        self.data: dict = dict()


    def get(self, position: int) -> Any | str:
        """ 
        parameter: position of the element you want get.
        returns: data at given position.
        """
        try:
            return self.data[position]
        except KeyError:
            return "No item found"


    def push_item(self, item: Any) -> None:
        """ 
        parameter: item to add the end of the array.
        returns: None
        """

        self.data[self.length] = item # Add element at end position.
        self.length += 1 # Add up counter.
        

    def pop_method(self) -> None:
        """ 
        This function does not receive any parameter since this method always removes last item of the array.
        returns: None
        """
        
        try:
            del self.data[self.length - 1]
            self.length -= 1
        except KeyError:
            return "Array is already empty..."


    
    def delete_item_at_index(self, index: int) -> None:
        """ 
        parameter: index of the item to remove.
        returns: None
        """
        while index < self.length - 1: # Iterate until last item is reached.
            self.data[index] = self.data[index + 1]  # At each iteration, update index of item.
            index += 1
        
        self.pop_method() # Remove last item to avoid repetition.
        self.length -= 1



if __name__ == "__main__":
    new_array = MyArray() # Instance of the class.
    print(new_array.get(0))
    

    new_array.push_item("a") # Add items.
    new_array.push_item("b")
    new_array.push_item("c")
    new_array.push_item("d")
    new_array.push_item("e")
    print(new_array.data) # Print out whole "array".

    
    new_array.pop_method() # Remove item.
    print(new_array.data)


    new_array.delete_item_at_index(1)
    print(new_array.data)


