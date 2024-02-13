#!usr/bin/python3

import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [23,32]
        result = summation(data)
        self.assertEqual(result, 55)

if _name_ == '_main_':
    unittest.main()
