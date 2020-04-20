"""This is a test file for us20.py
    Written by Fangji Liang   04/06/2020
"""

import unittest
from us20 import us20_a_u_marry_n_n
from ssw555Prj_Hogwarts import Repository

class Test_US20(unittest.TestCase):
    def test_us20_a_u_marry_n_n(self):
        test = Repository()
        self.assertEqual(us20_a_u_marry_n_n(test),[('ANOMALY', 'FAMILY', 'US20', 1062, '@F_L_US19_5@', 'Aunts and uncles should not marry their nieces or nephews')])
    
if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)