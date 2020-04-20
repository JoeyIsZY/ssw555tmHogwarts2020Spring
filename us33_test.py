"""This is a test file for us33.py
    Written by Fangji Liang   04/19/2020
"""

import unittest
from us34 import us34_large_age_couple
from us33 import us33_list_orphans
from ssw555Prj_Hogwarts import Repository

class Test_US20(unittest.TestCase):
    def test_us33(self):
        test = Repository()
        self.assertEqual(list(us33_list_orphans(test)), ['@I_W_US01_1@', '@I_H_US02_1@', '@I_H_US03_1@', '@I_Z_US05_1@', '@I_H_US12_3@', '@I_H_US12_4@', '@I_Z_US14_3@', '@I_Z_US14_4@', '@I_Z_US14_5@', '@I_Z_US14_6@', '@I_Z_US14_7@', '@I_Z_US14_8@', '@I_W_US35_1@'])
    
if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)