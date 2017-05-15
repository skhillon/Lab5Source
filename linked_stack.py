from linked_list import Pair, length

# A Stack is Stack(AnyList)
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
# Returns an empty Stack
def empty_stack():
    return Stack(None)

# Stack, Any -> Stack
# Adds a new value to the stack
def push(stack, new_val):
    return Stack(Pair(new_val, stack.any_list))

# Stack -> (Any, Stack)
# Returns the removed element and the resulting Stack; if there is no such element, raises IndexError
def pop(stack):
    if is_empty(stack):
        raise IndexError
    else:
        return (stack.any_list.value, Stack(stack.any_list.rest))

# Stack -> Any
# Returns the top element of the stack; if there is no such element, raises IndexError
def peek(stack):
    if is_empty(stack):
        raise IndexError
    else:
        return stack.any_list.value

# Stack -> int
# Returns number of elements in the stack
def size(stack):
    if is_empty(stack):
        return 0
    else:
        return length(stack.any_list)

# Stack -> Bool
# Checks if Stack is empty
def is_empty(stack):
    return stack.any_list is None