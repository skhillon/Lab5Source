import unittest
from linked_stack import *

class LinkedStackTests(unittest.TestCase):
    # Make new lists and stacks for every test case to avoid potential mutation problems

    def test_misc(self):
        # Put all the stuff you need for code coverage here
        pass

    def test_empty_stack(self):
        self.assertEqual(empty_stack(), Stack(None))

    def test_push(self):
        my_list  = Pair(4, Pair(3, Pair(2, Pair(1, None))))
        my_stack = Stack(my_list)

        pushed_list  = Pair(5, my_list)
        pushed_stack = Stack(pushed_list)

        self.assertEqual(push(empty_stack(), 5), Stack(Pair(5, None)))
        self.assertEqual(push(my_stack, 5), pushed_stack)

    def test_pop(self):
        my_list  = Pair(4, Pair(3, Pair(2, Pair(1, None))))
        my_stack = Stack(my_list)

        popped_list  = Pair(3, Pair(2, Pair(1, None)))
        popped_stack = Stack(popped_list)

        with self.assertRaises(IndexError):
            pop(empty_stack())

        self.assertEqual(pop(my_stack), (4, popped_stack))

    def test_peek(self):
        my_list  = Pair(4, Pair(3, Pair(2, Pair(1, None))))
        my_stack = Stack(my_list)

        with self.assertRaises(IndexError):
            peek(empty_stack())

        self.assertEqual(peek(my_stack), 4)

    def test_size(self):
        my_list  = Pair(4, Pair(3, Pair(2, Pair(1, None))))
        my_stack = Stack(my_list)

        self.assertEqual(size(empty_stack()), 0)
        self.assertEqual(size(my_stack), 4)

    def test_is_empty(self):
        my_list = Pair(4, Pair(3, Pair(2, Pair(1, None))))
        my_stack = Stack(my_list)

        self.assertTrue(is_empty(empty_stack()))
        self.assertFalse(is_empty(my_stack))

if __name__ == '__main__':
    unittest.main()