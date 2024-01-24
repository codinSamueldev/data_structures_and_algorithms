def constant_example(arr):
    """
    This function demonstrates constant time complexity O(1).
    It returns the first element of the given array.

    :param arr: List or array
    :return: The first element of the array
    """
    return arr[0]

# Example usage:
my_array = [1, 2, 3, 4, 5]
result = constant_example(my_array)
print(f"The first element is: {result}")
