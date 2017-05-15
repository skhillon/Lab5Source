import unittest
from array_stack import *

class ArrayStackTests(unittest.TestCase):
    # Make new lists and stacks for every test case to avoid potential mutation problems

    def test_misc(self):
        self.assertEqual(repr(Stack(List())), "Stack({})".format(repr(List())))

    def test_empty_stack(self):
        self.assertEqual(empty_stack(), Stack(List()))

    def test_push(self):
        my_list = List()
        my_list.array = [4, 3, 2, 1]
        my_list.length = 4

        my_stack = Stack(my_list)

        push(my_stack, 5)

        self.assertEqual(my_stack.any_list, my_list)

    def test_pop(self):
        my_list = List()
        my_list.array = [4, 3, 2, 1]
        my_list.length = 4
        
        my_stack = Stack(my_list)

        top_val, resultant_stack = pop(my_stack)

        compare_list = List()
        compare_list.array = [3, 2, 1]
        compare_list.length = 3

        compare_stack = Stack(compare_list)

        self.assertEqual(top_val, 4)
        self.assertEqual(resultant_stack, compare_stack)

        with self.assertRaises(IndexError):
            pop(empty_stack())

    def test_peek(self):
        my_list = List()
        my_list.array = [4, 3, 2, 1]
        my_list.length = 4
        
        my_stack = Stack(my_list)

        self.assertEqual(peek(my_stack), 4)

        with self.assertRaises(IndexError):
            peek(empty_stack())

    def test_size(self):
        my_list = List()
        my_list.array = [4, 3, 2, 1]
        my_list.length = 4
        
        my_stack = Stack(my_list)

        self.assertEqual(size(empty_stack()), 0)
        self.assertEqual(size(my_stack), 4)

    def test_is_empty(self):
        my_list = List()
        my_list.array = [4, 3, 2, 1]
        my_list.length = 4
        
        my_stack = Stack(my_list)

        self.assertTrue(is_empty(empty_stack()))
        self.assertFalse(is_empty(my_stack))

if __name__ == '__main__':
    unittest.main()