"""This is a test file for us18.py
    Written by Haodong Wu   02/25/2020
"""

import unittest
import os
import sys 
from us18 import us18_no_marriages_between_siblings
from ssw555Prj_Hogwarts import Repository

class Testno_marriages_to_children(unittest.TestCase):
    def test_us18_no_marriages_between_siblings(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us18_no_marriages_between_siblings(test),[('ANOMALY', 'FAMILY', 'US18', '471', '@F_W_US18_2@', 'Siblings @I_W_US18_3@ and @I_W_US18_4@ married')])
    
if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)
