def quadratic_example(arr):
    """
    This function demonstrates quadratic time complexity O(n^2).
    It prints all pairs of elements in the given array.

    :param arr: List or array
    """
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(f"Pair: ({arr[i]}, {arr[j]})")

# Example usage:
my_array = [1, 2, 3, 4, 5]
quadratic_example(my_array)
