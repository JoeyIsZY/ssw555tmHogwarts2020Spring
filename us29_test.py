"""This is a test file for us29.py
    Written by Ying Hu   11/04/2020
"""
import unittest
from us29 import us29_list_deceased
from ssw555Prj_Hogwarts import Repository


class Test_us29(unittest.TestCase):
    def test_list_deceased(self):
        test = Repository()
        self.assertEqual(us29_list_deceased(test), ('People who were deceased', ['@I1@', '@I2@', '@I3@', '@I4@', '@I5@',
                                                    '@I6@', '@I7@', '@I8@', '@I9@', '@I_W_US01_2@', '@I_W_US07_2@',
                                                    '@I_H_US02_1@', '@I_H_US02_2@', '@I_H_US03_1@', '@I_Z_US05_1@',
                                                    '@I_Z_US05_4@', '@I_L_US09_2@', '@I_L_US09_3@', '@I_W_US17_1@',
                                                    '@I_W_US17_2@', '@I_W_US17_3@', '@I_W_US18_1@', '@I_W_US18_2@',
                                                    '@I_W_US18_3@', '@I_W_US18_4@', '@I_H_US06_1@', '@I_H_US06_2@',
                                                    '@I_H_US12_1@', '@I_H_US12_2@', '@I_H_US12_3@', '@I_H_US12_4@',
                                                    '@I_H_US23_1@', '@I_H_US23_2@', '@I_W_US36_1@']))


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
