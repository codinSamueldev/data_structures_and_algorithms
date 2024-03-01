import random
from typing import Any

class BinarySearchTreeNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data: Any) -> None:
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self) -> list:
        array_sorted = list()

        if self.left:
            array_sorted += self.left.in_order_traversal()

        array_sorted.append(self.data)

        if self.right:
            array_sorted += self.right.in_order_traversal()

        return array_sorted
        

def build_tree(array: list) -> BinarySearchTreeNode:
    print("Array para convertir en arbol ->", array)
    root = BinarySearchTreeNode(array[0])

    for i in range(1, len(array)):
        root.add_child(array[i])

    return root
        

if __name__ == '__main__':
    random_array = [random.randint(1, 21) for _ in range(8)]

    create_tree = build_tree(random_array)
    print("El arbol binario ordenado es ->", create_tree.in_order_traversal())
