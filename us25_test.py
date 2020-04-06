"""This is a test file for us25.py
    Written by Haodong Wu   05/04/2020
"""
import unittest
import os
from us25 import us25_unique_first_names_in_families
from ssw555Prj_Hogwarts import Repository


class Testunique_first_names_in_families(unittest.TestCase):
    def test_unique_first_names_in_families(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us25_unique_first_names_in_families(test), 
                    [('ANOMALY', 'FAMILY', 'US25', 939, '@F_W_US25_1@', "Individuals ['@I_W_US25_3@', '@I_W_US25_4@'] have same name Sibling /Samename/ and same birthday 1996-01-01!")])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)