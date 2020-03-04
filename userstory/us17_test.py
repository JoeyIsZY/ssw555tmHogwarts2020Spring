"""This is a test file for us17.py
    Written by Haodong Wu   02/25/2020
"""
import unittest
import os
from us17 import us17_no_marriages_to_children
from ssw555Prj_Hogwarts import Repository

class Testno_marriages_to_children(unittest.TestCase):
    def test_us17_no_marriages_to_children(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us17_no_marriages_to_children(test),[('ANOMALY', 'FAMILY', 'US17', 424, '@F_W_US17_2@', 'Father @I_W_US17_1@ was married to child @I_W_US17_3@')])
    
if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)
