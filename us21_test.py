"""This is a test file for us21.py
    Written by Haodong Wu   05/04/2020
"""
import unittest
from us21 import us21_correct_gender_for_role
from ssw555Prj_Hogwarts import Repository


class Testcorrect_gender_for_role(unittest.TestCase):
    def test_correct_gender_for_role(self):
        test = Repository()
        self.assertEqual(us21_correct_gender_for_role(test), [('ANOMALY', 'FAMILY', 'US21', 887, '@F_W_US21_1@', 'Husband @I_W_US21_1@ in family @F_W_US21_1@ should be male'), 
                                                                ('ANOMALY', 'FAMILY', 'US21', 893, '@F_W_US21_1@', 'Wife @I_W_US21_2@ in family @F_W_US21_1@ should be female')])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)