"""
In the following code we are going to use common methods when working with arrays,
such as push, pop, unshift, etc...
"""
array_strings = ["a", "b", "c", "d"]
print(array_strings)


""" 
Push operation will always add new elements at the end of the array.
In Python, there is a built-in method called "append" that can perform push operation. 
This operation has a constant time O(1) in terms of time complexity.
"""
array_strings.append("e") # O(1)
print(array_strings)


"""
Pop operation will remove last element of the array, making this operation also linear in terms of time complexity.
"""
array_strings.pop() # O(1)
print(array_strings)


"""
Unshift operation allows to add element at the beginning of an array.
In Python, there is not an specific method which perform as exactly as the unshift operation does,
but we can use "insert" method, to replicate that.
Just so you know, the insert method needs two parameters, index and element to insert at that index.
"""
array_strings.insert(0, "z") # O(n)
print(array_strings)


