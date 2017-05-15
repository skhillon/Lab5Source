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

# AnyList, Any -> AnyList
# Mutates the input AnyList by adding an element to the end of its array
def append(any_list, new_val):
    check_array_size(any_list)
    any_list.array[array.length] = new_val
    any_list.array += 1
    return any_list

# AnyList -> None
# Mutates input AnyList by re-assigning array property to more None values
def check_array_size(any_list):
    if len(any_list.array) == any_list.length:
        new_array = [None] * any_list.length * 2

        for i in range(any_list.length):
            new_array[i] = any_list.array[i]
        any_list.array = new_array

# AnyList, int, Any -> AnyList
# Inserts an element into the specified index
def add(any_list, index, new_val):
    if index < 0 or index > any_list.length: 
        raise IndexError

    check_array_size(any_list)
    any_list.length += 1

    for i in range(any_list.length, index, -1):
        # start from the end and work your way down to above index
        any_list.array[i] = any_list.array[i-1]

    any_list.array[index] = new_val
    return any_list

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

    removed = any_list.array[index]

    for i in range(index, any_list.length):
        any_list.array[i] = any_list.array[i + 1]

    return removed, new_list