import unittest
from linked_stack import *

class LinkedStackTests(unittest.TestCase):

    def test_misc(self):
        # Put all the stuff you need for code coverage here
        pass

    def test_empty_stack(self):
        self.assertEqual(empty_stack(), Stack(None))

    def test_push(self):
        pass

    def test_pop(self):
        pass

    def test_peek(self):
        pass

    def test_size(self):
        pass

    def test_is_empty(self):
        my_list = Pair(4, Pair(3, Pair(2, Pair(1, None))))
        my_stack = Stack(my_list)

        self.assertTrue(is_empty(empty_stack()))
        self.assertFalse(is_empty(my_stack))

if __name__ == '__main__':
    unittest.main()