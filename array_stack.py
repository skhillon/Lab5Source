from array_list import List

# A Stack is Stack(List)
class Stack:
    def __init__(self, any_list):
        self.any_list = any_list

    def __eq__(self, other):
        return ((type(other) == Stack)
          and self.any_list == other.any_list
        )

    def __repr__(self):
        return ("Stack({!r})".format(self.any_list))

# None -> Stack
# Returns an empty stack
def empty_stack():
    return Stack(List())

# Stack, Any -> Stack
# Adds a new value to the stack
def push(stack, new_val):
    pass

# Stack -> (Any, Stack)
# Returns the removed element and the resulting Stack; if there is no such element, raises IndexError
def pop(stack):
    pass

# Stack -> Any
# Returns the top element of the stack; if there is no such element, raises IndexError
def peek(stack):
    pass

# Stack -> int
# Returns number of elements in the stack
def size(stack):
    pass

# Stack -> Bool
# Checks if Stack is empty
def is_empty(stack):
    pass

