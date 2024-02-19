""" LIFO - Last In First Out """
from typing import Any


class Node:
    """ A class representing a Node since we are going to use linked list. """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class Stack:
    """ A class representing Stack data structure. """
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    
    def peek(self) -> Node | Exception:
        """ See which node is at the top position. """
        if self.top is None and self.bottom:
            self.bottom = None
            raise Exception("Stack already empty :d")
        else:
            return self.top.data
    

    def push(self, data: Any) -> None:
        """ Add elements to top position. """
        NEW_NODE = Node(data)

        if self.top is None:
            self.top = NEW_NODE
            self.bottom = NEW_NODE
        else:
            NEW_NODE.next = self.top
            self.bottom = self.top.next
            self.top = NEW_NODE
        
        self.length += 1


    def pop(self) -> None:
        """ Remove the last inserted Node which should be top. """
        self.top = self.top.next
        self.length -= 1


    def isempty(self) -> bool:
        """ Check if stack is empty or not. """
        if self.length > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    stack_instance = Stack() # Instance stack class.

    # Add elements.
    stack_instance.push(1)
    stack_instance.push(2)
    stack_instance.push(3)

    # Remove elements and peek stack.
    stack_instance.pop()
    print(f"Current top -> {stack_instance.peek()}, bottom -> {stack_instance.bottom.data}\n")
    stack_instance.pop()

    # Remove last element, check if method is working, and force exception get raised.
    stack_instance.pop()
    print(f"Stack length -> {stack_instance.length}", stack_instance.isempty())
    print(stack_instance.peek())
