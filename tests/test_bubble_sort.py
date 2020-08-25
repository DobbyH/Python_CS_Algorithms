import unittest
from sort.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_b_sort_fails_with_empty_list(self):
        empty_list = []
        self.assertEqual(
            bubble_sort(empty_list),
            -1
        )

    def test_list_sort(self):
        unordered_list = [4,3,2,1]
        self.assertEqual(
            bubble_sort(unordered_list),
            [1,2,3,4]
        )

    def test_lager_list_sort(self):
        unordered_list = [43,5,21,4,76,2,4,24,43,32,2,1]
        self.assertEqual(
            bubble_sort(unordered_list),
            [1, 2, 2, 4, 4, 5, 21, 24, 32, 43, 43, 76]
        )
