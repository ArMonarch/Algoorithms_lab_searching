import unittest
from datetime import datetime, time
from Linear_Search import Linear_Search
# from Linear_Search_Data import Linear_Search_Data

class Test_Linear_Search(unittest.TestCase):
    test_data: list[int] = list(range(0,10000))

    def test_Linear_Search_01(self):
        # for best case
        # search first element of the list
        (search_key, search_key_index) = 0, 0
        searched_index:int = Linear_Search(DATA_ARRAY=self.test_data, KEY=search_key)
        self.assertEqual(searched_index, search_key_index)
    
    def test_Linear_Search_02(self):
        # for Average case
        # search appox. middle element of the list
        (search_key, search_key_index) = 5000, 5000
        searched_index:int = Linear_Search(DATA_ARRAY=self.test_data, KEY=search_key)
        self.assertEqual(searched_index, search_key_index)
    
    def test_Linear_Search_03(self):
        # for Worst Case
        # search last element of the list
        (search_key, search_key_index) = 9999, 9999
        searched_index:int = Linear_Search(DATA_ARRAY=self.test_data, KEY=search_key)
        self.assertEqual(searched_index, search_key_index)
    
    def test_Linear_Search_04(self):
        # search empty list 
        # the value must be -1
        searched_index:int = Linear_Search(DATA_ARRAY=list(), KEY=0)
        self.assertEqual(searched_index, -1)
    
    def test_Linear_Search_015(self):
        # search element that is not  in the list
        searched_index:int = Linear_Search(DATA_ARRAY=self.test_data, KEY=1000000000)
        self.assertEqual(searched_index, -1)

        

if __name__ == "__main__":
    unittest.main()
