from typing import Any

class Node:
    """ A class representing a linked list node. """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class Queue:
    """ A class representing a queue data structure. """
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0


    def peek(self) -> Node | None:
        """ See which node was the first queueing. Time complexity O(1). """
        return self.first.data


    def enqueue(self, data: Any) -> None:
        """ Add Nodes to the queue. Time complexity O(1). """
        NEW_NODE = Node(data=data)

        if self.first is None:
            # If queue is empty, then update first and last value.
            self.first = NEW_NODE
            self.last = NEW_NODE
        else:
            # Otherwise, current next last node will point to the new node and update last value.
            self.last.next = NEW_NODE
            self.last = NEW_NODE

        self.length += 1


    def dequeue(self) -> None | Exception:
        """ Remove the first in node. Time complexity O(1). """
        try:
            self.first = self.first.next
            if self.first is None:
                self.last = None
                return
        except:
            raise Exception("Sorry, queue already empty ;c")
        
        self.length -= 1


    def isempty(self) -> bool:
        if self.length > 1:
            return False
        else:
            return True


    def print_out_queue(self) -> str:
        """ Print out the whole queue. """

        if self.first is None:
            # If queue is empty, print according info and prevent rest of code be executed.
            print("Nothing to show, queue is empty...")
            return

        iterator = self.first

        while iterator is not None:
            print(iterator.data, "-->", end=" ")

            iterator = iterator.next

        return "Done"
    

if __name__ == '__main__':
    queue_instance = Queue() # Queue instance.

    # Add elements to queue.
    queue_instance.enqueue(1)
    queue_instance.enqueue(2)
    queue_instance.enqueue(3)

    # Remove first element inserted in the queue.
    queue_instance.dequeue()
    queue_instance.dequeue()
    queue_instance.dequeue()

    # Finally, print out the whole queue.
    queue_instance.print_out_queue()

    print(queue_instance.isempty())