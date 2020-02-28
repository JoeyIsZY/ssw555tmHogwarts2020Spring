"""This is a test file for us01.py
    Written by Haodong Wu   02/15/2020
"""
import unittest
import os
from us01 import us01_current_date_check
from ssw555Prj_Hogwarts import Repository


class Testcurrent_date_check(unittest.TestCase):
    def test_current_date_check(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(current_date_check(test), [('ERROR', 'INDIVIDUAL', 'US01', 119, '@I_W_US01_1@', 'Birthday 2021-01-01 occurs in the future.'), 
                                                    ('ERROR', 'INDIVIDUAL', 'US01', 127, '@I_W_US01_2@', 'DEATH 2081-12-30 occurs in the future.'), 
                                                    ('ERROR', 'FAMILY', 'US01', 201, '@F_W_US01_1@', 'Marriage date 2040-02-21 occurs in the future.'), 
                                                    ('ERROR', 'FAMILY', 'US01', 203, '@F_W_US01_1@', 'Divorce date 2070-01-01 occurs in the future.')])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)
