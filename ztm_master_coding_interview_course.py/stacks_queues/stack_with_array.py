from typing import Any


class Stack:
    """ A class representing a stack data structure. """
    def __init__(self) -> None:
        """ Use array/list to store data. """
        self.data = list()

    
    def peek(self) -> Any:
        """ See last element stored. """
        return self.data[-1]
    

    def push(self, data: Any) -> None:
        """ Add elements at top position. """
        self.data.append(data)

    
    def pop(self) -> None:
        """ Remove last element stored. """
        try:
            self.data.pop()
        except:
            raise Exception("Stack already empty :d")


    def isempty(self) -> bool:
        """ Check if stack is empty. """
        if len(self.data) > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    stack_array = Stack() # Instance stack class.

    # Add some elements.
    stack_array.push("Google")
    stack_array.push("Udemy")
    stack_array.push("Discord")

    # See which element is placed at the top position, and print out stack.
    print(f"Current top -> {stack_array.peek()} | Stack data -> {stack_array.data}\n")

    # Delete elements.
    stack_array.pop()
    stack_array.pop()
    stack_array.pop()

    # Print stack and check if is empty.
    print(stack_array.data, stack_array.isempty())
