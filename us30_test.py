"""This is a test file for us30.py
    Written by Ying Hu   11/04/2020
"""
import unittest
from us30 import us30_list_living_married
from ssw555Prj_Hogwarts import Repository


class Test_us30(unittest.TestCase):
    def test_list_living_married(self):
        test = Repository()
        self.assertEqual(us30_list_living_married(test), ('People who are living and married', ['@I1@', '@I2@', '@I3@', '@I4@',
                                                          '@I6@', '@I_W_US01_2@', '@I_H_US03_1@', '@I_Z_US05_1@',
                                                          '@I_Z_US05_4@', '@I_L_US09_2@', '@I_L_US09_3@',
                                                          '@I_W_US17_1@', '@I_W_US17_2@', '@I_W_US18_1@',
                                                          '@I_W_US18_2@', '@I_W_US18_3@', '@I_W_US18_4@',
                                                          '@I_H_US23_1@', '@I_H_US23_2@']))


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
