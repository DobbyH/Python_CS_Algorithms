import unittest
from sort.quick_sort import quick_sort

class TestQucikSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_q_sort_fails_with_empty_list(self):
        empty_list = []
        self.assertEqual(
            quick_sort(empty_list),
            -1
        )

    def test_list_sort(self):
        unordered_list = [4,3,2,1]
        self.assertEqual(
            quick_sort(unordered_list),
            [1,2,3,4]
        )

    def test_lager_list_sort(self):
        unordered_list = [50,40,30,20,10,1]
        self.assertEqual(
            quick_sort(unordered_list),
            [1,10,20,30,40,50]
        )
