# An AnyList is one of:
# - None
# - Pair(value, AnyList)
class Pair:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest

    def __eq__(self, other):
        return ((type(other) == Pair)
          and self.value == other.value
          and self.rest == other.rest
        )

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.value, self.rest))

# None -> AnyList
# Creates an empty AnyList
def empty_list():
    return None

# AnyList, int, Value -> AnyList
# Inserts a Value into AnyList at an integer Index
def add(any_list, index, value):
    if any_list == None:
        if index == 0:
            return Pair(value, None)
        else:
            raise IndexError
    else:
        if index == 0:
            return Pair(value, any_list)
        else:
            return Pair(any_list.value, add(any_list.rest, index - 1, value))

# AnyList -> Int
# Returns length of AnyList
def length(any_list):
    if any_list == None:
        return 0
    else:
        return 1 + length(any_list.rest)

# AnyList, int -> Value
# Gets the Value at an Index in AnyList
def get(any_list, index):
    if any_list == None or index < 0:
        raise IndexError
    else:
        if index == 0:
            return any_list.value
        else:
            return get(any_list.rest, index - 1)

# AnyList, int, Value -> AnyList
# Sets the Value at an Index
def set(any_list, index, value):
    if index < 0:
        raise IndexError
    else:
        if any_list == None and index == 0:
            return Pair(value, None)
        elif any_list != None and index == 0:
            return Pair(value, any_list.rest)
        else:
            return Pair(any_list.value, set(any_list.rest, index - 1, value))

# AnyList, Index -> (Any, AnyList)
# Removes an element at an Index and returns a tuple with the removed element and the resulting list
def remove(any_list, index):
    if any_list == None or index < 0:
        raise IndexError
    if index == 0:
        return any_list.value, any_list.rest

    result = remove(any_list.rest, index - 1)
    return result[0], Pair(any_list.value, result[1])