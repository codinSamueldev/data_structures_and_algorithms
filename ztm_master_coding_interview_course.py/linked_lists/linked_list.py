from typing import Any

class Node:
    """ Create a separated class to store data into nodes. """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def prepend(self, data: Any) -> None:
        """ Add nodes to head. Time complexity O(1). """
        if self.head is None:
            add_node = Node(data=data)
            self.head = add_node
        else:
            add_node = Node(data=data)
            add_node.next = self.head
            self.head = add_node

    
    def print_out_linked_list(self) -> str | False:
        """ 
        Print out all nodes in the linked list. 
        Last node references to a None value.
        Lastly, if Linked List is empty, return False value.
        """
        if self.head is None:
            print("Sorry, linked list does not has info :(")
            return False

        while self.head is not None:
            print(self.head.data, ' --> ', end=' ')
            self.head = self.head.next
            if self.head is None:
                print(None, end=' ')
        
        print('\nExecution completed successfully :D')



if __name__ == '__main__':
    my_linked_list = LinkedList() # Instance of LinkedList class.
    
    # Add nodes to head.
    my_linked_list.prepend(10)
    my_linked_list.prepend(5)
    my_linked_list.prepend(15)
    my_linked_list.prepend("Tiburoncin uahah")
    
    # Print out linked list.
    my_linked_list.print_out_linked_list()


