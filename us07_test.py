"""This is a test file for us07.py
    Written by Haodong Wu   02/15/2020
"""
import unittest
import os
from us07 import not_olderthan150
from ssw555Prj_Hogwarts import Repository




class Testcurrent_date_check(unittest.TestCase):
    def test_not_olderthan150(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(not_olderthan150(test), [('ERROR', 'INDIVIDUAL', 'US07', 133, '@I_W_US07_1@', 'More than 150 years old - Birth date: 1860-01-01.'), 
                                                ('ERROR', 'INDIVIDUAL', 'US07', 138, '@I_W_US07_2@', 'More than 150 years old at death - Birth date: 1850-01-01, Death date: 2005-01-02.')])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)