# An ArrayList is List()
class List:
    def __init__(self):
        self.array = [None]*10
        self.length = 0
        self.capacity = 10

    def __eq__(self, other):
        return ((type(other) == List)
          and self.array == other.array
          and self.length == other.length
          and self.capacity == other.capacity
        )

    def __repr__(self):
        return ("List({!r}, {!r}, {!r})".format(self.array, self.length, self.capacity))

# None -> List
# Creates an empty list
def empty_list():
    return List()

# ArrayList, int, Any -> ArrayList
# Inserts a value into ArrayList at given index
def add(any_list, index, value):
    if index < 0 or index > any_list.length:
        raise IndexError

    new_list = List()
    new_list.length = any_list.length + 1
    new_list.capacity = index * 2
    new_list.array = [None] * index * 2

    for i in range(index):
        new_list.array[i] = any_list.array[i]

    new_list.array[index] = value

    for j in range(index, any_list.length):
        new_list.array[j + 1] = any_list.array[j]

    return new_list

# AnyList -> int
# Returns length of array
def length(any_list):
    return any_list.length

# AnyList, int -> Any
# Gets the value at a given Index
def get(any_list, index):
    if index < 0 or index >= any_list.length:
        raise IndexError
    
    return any_list.array[index]
    
# AnyList, int, Any -> AnyList
# Sets the value at Index to given value
def set(any_list, index, value):
    if index < 0 or index >= any_list.length:
        raise IndexError
    
    any_list.array[index] = value
    return any_list

# AnyList, int -> Any, AnyList
# Removes the element at specified Index and returns a tuple containing the removed element and the resulting list
def remove(any_list, index):
    if index >= any_list.length or index < 0:
        raise IndexError
    
    new_list = List()
    new_list.length = any_list.length - 1

    for i in range(index):
        new_list.array[i] = any_list.array[i]

    removed = any_list.array[index]

    for j in range(index + 1, any_list.length):
        new_list.array[j - 1] = any_list.array[j]

    return removed, new_list