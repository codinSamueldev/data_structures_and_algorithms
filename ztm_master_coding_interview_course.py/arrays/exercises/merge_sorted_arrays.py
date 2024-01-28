

def merge_arrays(array1: list, array2: list) -> list: # O(n + m).
    
    solution = list()
    
    for item in array1:
        solution.append(item)
    
    
    for item2 in array2:
        solution.append(item2)
    
    return sorted(solution)


def merge_arrays2(array1: list, array2: list) -> list: # O(n log n).
    
    if len(array1) > 1 and len(array2) > 1:
        solution = array1 + array2
        return sorted(solution)
    else:
        raise IndexError("Provide at least one item.")

    
if __name__ == "__main__":
    # print(merge_arrays([1,3,4,7], [2,4,5,6]))
    
    print(merge_arrays2([1,3,4,7], [2,4,5,6]))

