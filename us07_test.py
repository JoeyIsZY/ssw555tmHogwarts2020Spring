"""This is a test file for us07.py
    Written by Haodong Wu   02/15/2020
"""
import unittest
from us07 import not_olderthan150
from P03_Hogwarts_V2 import Repository




class Testcurrent_date_check(unittest.TestCase):
    def test_not_olderthan150(self):
        test = Repository()
        test.get_file_reader()
        test.update_individuals()
        test.update_families()
        self.assertEqual(not_olderthan150(test), ['ERROR! at line 33, the individual who was born at 11 FEB 0513 is 187 years old.', 
                                                    'ERROR! at line 44, the individual who was born at 10 APR 1850 is 169 years old.'])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)