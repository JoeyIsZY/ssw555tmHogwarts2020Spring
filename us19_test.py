"""This is a test file for us19.py
    Written by Fangji Liang   04/06/2020
"""

import unittest
import os
import sys 
from us19 import us19_first_cousin_not_marry
from ssw555Prj_Hogwarts import Repository

class Test_US19(unittest.TestCase):
    def test_us19_first_cousin_not_marry(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us19_first_cousin_not_marry(test),[('ANOMALY', 'FAMILY', 'US19', 1057, '@F_L_US19_4@', 'First cousins should not marry')])
    
if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)