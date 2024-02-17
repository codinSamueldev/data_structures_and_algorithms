from typing import Any

class Node:
    """ A class representing a node in a linked list. """
    def __init__(self, data):
        """ Initialize the node with the given data. """
        self.data = data
        self.previous = None
        self.next = None


class LinkedList:
    """ A class representing a doubly linked list. """
    def __init__(self):
        """ Initialize an empty doubly linked list. """
        self.head = None
        self.tail = None


    def prepend(self, data: Any) -> None:
        """ Add nodes to head. Time complexity O(1). """
        ADD_NODE = Node(data=data)
        if self.head is None:
            self.head = ADD_NODE
            self.tail = ADD_NODE
        else:
            ADD_NODE.next = self.head
            self.head.previous = ADD_NODE
            self.head = ADD_NODE


    def append_nodes(self, data: Any) -> None:
        """ Add a node with the given data to the end of the list. Time complexity O(1). """
        ADD_NODE = Node(data)

        if self.head is None:
            self.prepend(ADD_NODE)
        else:
            ADD_NODE.previous = self.tail
            self.tail.next = ADD_NODE
            self.tail = ADD_NODE


    def insert_node_at(self, index: int, data: Any) -> None:
        """ Insert a node with the given data at the specified index. Time complexity O(n). """
        ADD_NODE = Node(data=data)
        count = 0
        iterator = self.head

        if index < 0:
            raise IndexError("Positive integers only...")
        elif index == 0:
            self.prepend(data)

        while iterator is not None:
            if count == index:
                ADD_NODE.next = iterator
                ADD_NODE.previous = iterator.previous
                iterator.previous.next = ADD_NODE
                return

            count += 1
            iterator = iterator.next

        raise Exception("Sorry, linked list out of bounds...")


    def print_out_linked_list(self) -> str | bool:
        """
        Print out all nodes in the linked list.
        Last node references to a None value.
        Lastly, if Linked List is empty, return False value.
        """
        if self.head is None:
            print("Sorry, linked list does not has info :(")
            return False

        while self.head is not None:
            print(self.head.data, '<-->', end=' ')
            self.head = self.head.next
            if self.head is None:
                print(None, end=' ')

        print('\nExecution completed successfully :D')



if __name__ == '__main__':
    my_linked_list = LinkedList() # Instance of LinkedList class.

    # Add nodes to the beginning and end of the list.
    my_linked_list.prepend(10)
    my_linked_list.prepend(5)
    my_linked_list.prepend(15)
    my_linked_list.prepend(20)
    my_linked_list.append_nodes("Last")
    my_linked_list.append_nodes("bYE")

    # Insert a node at a specific index.
    my_linked_list.insert_node_at(5, "I am here")

    # Print out linked list.
    my_linked_list.print_out_linked_list()