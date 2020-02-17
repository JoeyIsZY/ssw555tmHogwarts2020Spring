"""This is a test file for us01.py
    Written by Haodong Wu   02/15/2020
"""
import unittest
from us01 import current_date_check
from P03_Hogwarts_V2 import Repository




class Testcurrent_date_check(unittest.TestCase):
    def test_current_date_check(self):
        test = Repository()
        test.get_file_reader()
        test.update_individuals()
        test.update_families()
        self.assertEqual(current_date_check(test), ['ERROR! The birth date at line 22 is 10 JAN 2021 after now.',
                                                    'ERROR! The death date at line 24 is 14 NOV 2088 after now.', 
                                                    'ERROR! The marriage date at line 119 is 21 JUL 2033 after now.',
                                                    'ERROR! The divorce date at line 121 is 1 JUL 2100 after now.'])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)