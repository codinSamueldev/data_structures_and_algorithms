
from typing import Any


class HashTable:
    def __init__(self, size: int) -> None:
        self.data = list(range(size))


    def set_data(self, data_to_give: list) -> None:
        """ Insert values if there is space available, if not raise error. The space is given on constructor method."""
        for index, value in enumerate(self.data):
            if type(value) == int:  # If there is space, insert at space available the data given.
                self.data[index] = data_to_give
                break

            if type(self.data[-1]) == list:  # Raise error if last data given exceed space capacity.
                raise IndexError("There is not more space, remove last item provided...")


    def get_value(self, key: Any) -> None:
        """ Print out item value if key exists, if not raise error. """
        found = False

        for i in self.data:
            if i[0] == key:
                found = True
                print(i[1], "\n")
                break

        if not found:
            raise KeyError("Item not found...")



if __name__ == "__main__":
    test = HashTable(3)

    test.set_data(["Apples", 987])
    test.set_data(["Dragonfruits", 1111])
    test.set_data(["Oranges", 324])
    # test.set_value("nope")

    test.get_value("Oranges")

    print(test.data)
