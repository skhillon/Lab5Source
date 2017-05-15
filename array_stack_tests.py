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

        pass

if __name__ == '__main__':
    unittest.main()



