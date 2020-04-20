"""This is a test file for us34.py
    Written by Fangji Liang   04/19/2020
"""

import unittest
from us34 import us34_large_age_couple
from ssw555Prj_Hogwarts import Repository

class Test_US20(unittest.TestCase):
    def test_us34(self):
        test = Repository()
        self.assertEqual(list(us34_large_age_couple(test)), [{'HUSB': '@I_W_US01_1@', 'WIFE': '@I_W_US01_2@'}, {'HUSB': '@I_H_US02_1@', 'WIFE': '@I_H_US02_2@'}, {'HUSB': '@I_W_US17_1@', 'WIFE': '@I_W_US17_3@'}])
    
if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)