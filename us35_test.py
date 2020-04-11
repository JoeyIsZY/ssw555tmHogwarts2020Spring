"""This is a test file for us35.py
    Written by Haodong Wu   10/04/2020
"""
import unittest
import os
from us35 import us35_list_recent_births
from ssw555Prj_Hogwarts import Repository


class Testlist_recent_births(unittest.TestCase):
    def test_list_recent_births(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us35_list_recent_births(test), ('People who were born in the last 30 days', ['@I_W_US35_1@']) )

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)