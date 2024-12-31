import unittest
from datetime import datetime
from Binary_Search import Binary_Search
# from Binary_Search_Data import Binary_Search_Data

class Test_Binary_Search(unittest.TestCase):
    test_data: list[int] = list(range(0,10000))

    def test_Binary_Search_01(self):
        # for best case
        # search middle element of the list
        (search_key, search_key_index) = 4999, 4999
        searched_index:int = Binary_Search(DATA_ARRAY=self.test_data, KEY=search_key)
        self.assertEqual(searched_index, search_key_index)

    def test_Binary_Search_02(self):
        # for Average Case
        # search any element of the list expect middle element or start, end element
        (search_key, search_key_index) = 2000, 2000
        searched_index:int = Binary_Search(DATA_ARRAY=self.test_data, KEY=search_key)
        self.assertEqual(searched_index, search_key_index)

    def test_Binary_Search_03(self):
        # for Worst Case
        # search start or end element of the list
        (search_key, search_key_index) = 0, 0
        searched_index:int = Binary_Search(DATA_ARRAY=self.test_data, KEY=search_key)
        self.assertEqual(searched_index, search_key_index)

   # def test_Binary_Search_04(self):
   #     # for empty list as input
   #     searched_index:int = Binary_Search(DATA_ARRAY=list(), KEY=0)
   #     self.assertEqual(searched_index, -1)

   # def test_Binary_Search_05(self):
   #     # for empty list as input
   #     searched_index:int = Binary_Search(DATA_ARRAY=self.test_data, KEY=10000)
   #     self.assertEqual(searched_index, -1)

if __name__ == "__main__":
    unittest.main()
