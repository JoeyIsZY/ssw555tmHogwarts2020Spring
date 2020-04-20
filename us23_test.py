"""This is a test file for us23.py
    Written by Ying Hu   03/30/2020
"""
import unittest
from us23 import us23_unique_name_birth_date
from ssw555Prj_Hogwarts import Repository


class Test_us23_unique_name_birth_date(unittest.TestCase):
    def test_us23_unique_name_birth_date(self):
        test = Repository()
        # Get returned list sorted to match the result
        self.assertEqual(us23_unique_name_birth_date(test),
                         [('ANOMALY', 'INDIVIDUAL', 'US23', (783, 794), ('@I_H_US23_1@', '@I_H_US23_2@'),
                           'Individuals have same name and birth date'), 
                           ('ANOMALY', 'INDIVIDUAL', 'US23', (916, 922), ('@I_W_US25_3@', '@I_W_US25_4@'), 
                           'Individuals have same name and birth date')])


if __name__ == '__main__':
    unittest.main()

