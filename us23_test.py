"""This is a test file for us23.py
    Written by Ying Hu   03/30/2020
"""
import unittest
import os
from us23 import us23_unique_name_birth_date
from ssw555Prj_Hogwarts import Repository


class Test_us23_unique_name_birth_date(unittest.TestCase):
    def test_us23_unique_name_birth_date(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        # Get returned list sorted to match the result
        self.assertEqual(us23_unique_name_birth_date(test),
                         [('ANOMALY', 'INDIVIDUAL', 'US23', (701, 712), ('@I_H_US23_1@', '@I_H_US23_2@'),
                           'Individuals have same name and birth date')])


if __name__ == '__main__':
    unittest.main()
