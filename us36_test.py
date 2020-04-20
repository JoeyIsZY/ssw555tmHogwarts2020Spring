"""This is a test file for us36.py
    Written by Haodong Wu   10/04/2020
"""
import unittest
from us36 import us36_list_recent_deaths
from ssw555Prj_Hogwarts import Repository


class Testlist_recent_deaths(unittest.TestCase):
    def test_list_recent_deaths(self):
        test = Repository()
        self.assertEqual(us36_list_recent_deaths(test), ('People who were died in the last 30 days', ['@I_W_US36_1@']) )

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)