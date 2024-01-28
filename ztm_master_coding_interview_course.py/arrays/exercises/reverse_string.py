"""
Create a function which takes a string as parameter, and return the string reversed.

Example 1:
Input -> Samuel
Output -> leumaS

Example 2:
Input -> I am a millonaire
Output -> erianollim a ma I
"""


def reverse_string(word: str) -> str: # O(1).
    return word[::-1]
    

def reverse_string2(word: str) -> str: # 0(n).
    
    solution = str()
    length = len(word) - 1
    
    while length >= 0:
        solution += word[length]
        length -= 1
        
    return solution
    
    
if __name__ == "__main__":
    # print(reverse_string("Samuel"))

    print(reverse_string2("I am a millonaire"))

